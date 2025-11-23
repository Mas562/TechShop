from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Cart, CartItem, Order, OrderItem


def home(requ):
    featured_products = Product.objects.filter(available=True)[:6]
    categories = Category.objects.all()[:6]
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(requ, 'shop/home.html', context)


def product_list(requ):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    category_slug = requ.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    query = requ.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'query': query,
    }
    return render(requ, 'shop/product_list.html', context)


def product_detail(requ, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(requ, 'shop/product_detail.html', context)


def category_products(requ, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()

    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(requ, 'shop/category_products.html', context)


def get_or_create_cart(requ):
    if requ.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=requ.user)
    else:
        session_key = requ.session.session_key
        if not session_key:
            requ.session.create()
            session_key = requ.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


def cart_detail(requ):
    cart = get_or_create_cart(requ)
    context = {'cart': cart}
    return render(requ, 'shop/cart_detail.html', context)


def add_to_cart(requ, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(requ)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(requ, f'{product.name} добавлен в корзину')
    return redirect('shop:cart_detail')


def update_cart(requ, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if requ.method == 'POST':
        quantity = int(requ.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(requ, 'Количество обновлено')
        else:
            cart_item.delete()
            messages.success(requ, 'Товар удалён из корзины')

    return redirect('shop:cart_detail')


def remove_from_cart(requ, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(requ, 'Товар удалён из корзины')
    return redirect('shop:cart_detail')


@login_required
def checkout(requ):
    cart = get_or_create_cart(requ)

    if not cart.items.exists():
        messages.warning(requ, 'Корзина пуста')
        return redirect('shop:cart_detail')

    if requ.method == 'POST':
        order = Order.objects.create(
            user=requ.user,
            first_name=requ.POST.get('first_name'),
            last_name=requ.POST.get('last_name'),
            email=requ.POST.get('email'),
            phone=requ.POST.get('phone'),
            address=requ.POST.get('address'),
            total_price=cart.get_total_price()
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

        cart.items.all().delete()
        messages.success(requ, f'Заказ #{order.id} успешно создан!')
        return redirect('shop:order_success', order_id=order.id)

    context = {'cart': cart}
    return render(requ, 'shop/checkout.html', context)


@login_required
def order_success(requ, order_id):
    order = get_object_or_404(Order, id=order_id, user=requ.user)
    context = {'order': order}
    return render(requ, 'shop/order_success.html', context)


@login_required
def order_list(requ):
    orders = Order.objects.filter(user=requ.user)
    context = {'orders': orders}
    return render(requ, 'shop/order_list.html', context)