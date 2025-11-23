from .models import Cart


def cart_count(requ):
    cart_items_count = 0

    if requ.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=requ.user)
            cart_items_count = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            pass
    else:
        session_key = requ.session.session_key
        if session_key:
            try:
                cart = Cart.objects.get(session_key=session_key)
                cart_items_count = sum(item.quantity for item in cart.items.all())
            except Cart.DoesNotExist:
                pass

    return {'cart_items_count': cart_items_count}