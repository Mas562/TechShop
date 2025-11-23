from django.core.management.base import BaseCommand
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу'

    def handle(self, *args, **kwargs):
        self.stdout.write('Загрузка тестовых данных...')

        # Создание категорий
        categories_data = [
            {
                'name': 'Смартфоны',
                'slug': 'smartphones',
                'description': 'Современные смартфоны от ведущих производителей'
            },
            {
                'name': 'Ноутбуки',
                'slug': 'laptops',
                'description': 'Ноутбуки для работы, учебы и развлечений'
            },
            {
                'name': 'Планшеты',
                'slug': 'tablets',
                'description': 'Планшеты для любых задач'
            },
            {
                'name': 'Наушники',
                'slug': 'headphones',
                'description': 'Наушники и гарнитуры'
            },
            {
                'name': 'Умные часы',
                'slug': 'smartwatches',
                'description': 'Смарт-часы и фитнес-браслеты'
            },
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description']
                }
            )
            categories[cat_data['slug']] = cat
            status = 'создана' if created else 'уже существует'
            self.stdout.write(f'Категория "{cat.name}" {status}')

        # Создание товаров
        products_data = [
            {
                'category': 'smartphones',
                'name': 'Samsung Galaxy S24 Ultra',
                'slug': 'samsung-galaxy-s24-ultra',
                'description': 'Флагманский смартфон с 6.8" дисплеем, процессором Snapdragon 8 Gen 3, 12GB RAM, 256GB памяти и камерой 200MP',
                'price': 119990,
                'stock': 15
            },
            {
                'category': 'smartphones',
                'name': 'iPhone 15 Pro Max',
                'slug': 'iphone-15-pro-max',
                'description': 'Премиальный смартфон Apple с титановым корпусом, чипом A17 Pro, 256GB памяти и продвинутой камерой',
                'price': 134990,
                'stock': 12
            },
            {
                'category': 'smartphones',
                'name': 'Xiaomi 14 Pro',
                'slug': 'xiaomi-14-pro',
                'description': 'Мощный смартфон с Snapdragon 8 Gen 3, 12GB RAM, 512GB памяти и камерой Leica',
                'price': 89990,
                'stock': 20
            },
            {
                'category': 'smartphones',
                'name': 'Google Pixel 8 Pro',
                'slug': 'google-pixel-8-pro',
                'description': 'Смартфон с чистым Android, процессором Tensor G3 и выдающимися камерами',
                'price': 94990,
                'stock': 10
            },
            {
                'category': 'laptops',
                'name': 'MacBook Pro 16" M3 Pro',
                'slug': 'macbook-pro-16-m3-pro',
                'description': 'Профессиональный ноутбук с чипом M3 Pro, 18GB RAM, 512GB SSD и дисплеем Liquid Retina XDR',
                'price': 289990,
                'stock': 8
            },
            {
                'category': 'laptops',
                'name': 'Dell XPS 15',
                'slug': 'dell-xps-15',
                'description': 'Премиальный ноутбук с Intel Core i7-13700H, 16GB RAM, 1TB SSD и дисплеем 4K',
                'price': 179990,
                'stock': 10
            },
            {
                'category': 'laptops',
                'name': 'ASUS ROG Zephyrus G16',
                'slug': 'asus-rog-zephyrus-g16',
                'description': 'Игровой ноутбук с Intel Core i9, NVIDIA RTX 4070, 32GB RAM и экраном 240Hz',
                'price': 249990,
                'stock': 6
            },
            {
                'category': 'laptops',
                'name': 'Lenovo ThinkPad X1 Carbon',
                'slug': 'lenovo-thinkpad-x1-carbon',
                'description': 'Бизнес-ноутбук с Intel Core i7, 16GB RAM, 512GB SSD и легким корпусом',
                'price': 159990,
                'stock': 12
            },
            {
                'category': 'tablets',
                'name': 'iPad Pro 12.9" M2',
                'slug': 'ipad-pro-129-m2',
                'description': 'Мощный планшет с чипом M2, 256GB памяти и дисплеем Liquid Retina XDR',
                'price': 119990,
                'stock': 15
            },
            {
                'category': 'tablets',
                'name': 'Samsung Galaxy Tab S9 Ultra',
                'slug': 'samsung-galaxy-tab-s9-ultra',
                'description': 'Большой планшет с 14.6" AMOLED дисплеем, 12GB RAM и S Pen в комплекте',
                'price': 99990,
                'stock': 10
            },
            {
                'category': 'tablets',
                'name': 'Xiaomi Pad 6 Pro',
                'slug': 'xiaomi-pad-6-pro',
                'description': 'Планшет с Snapdragon 8+ Gen 1, 8GB RAM, 256GB памяти и 11" дисплеем 120Hz',
                'price': 44990,
                'stock': 18
            },
            {
                'category': 'headphones',
                'name': 'Sony WH-1000XM5',
                'slug': 'sony-wh-1000xm5',
                'description': 'Премиальные беспроводные наушники с активным шумоподавлением',
                'price': 34990,
                'stock': 25
            },
            {
                'category': 'headphones',
                'name': 'AirPods Pro 2',
                'slug': 'airpods-pro-2',
                'description': 'Беспроводные наушники Apple с активным шумоподавлением и пространственным звуком',
                'price': 26990,
                'stock': 30
            },
            {
                'category': 'headphones',
                'name': 'Bose QuietComfort Ultra',
                'slug': 'bose-quietcomfort-ultra',
                'description': 'Наушники с превосходным шумоподавлением и комфортной посадкой',
                'price': 39990,
                'stock': 15
            },
            {
                'category': 'headphones',
                'name': 'JBL Tune 760NC',
                'slug': 'jbl-tune-760nc',
                'description': 'Доступные беспроводные наушники с шумоподавлением и 50 часами работы',
                'price': 7990,
                'stock': 40
            },
            {
                'category': 'smartwatches',
                'name': 'Apple Watch Series 9',
                'slug': 'apple-watch-series-9',
                'description': 'Умные часы с двойным касанием, ярким дисплеем и расширенными функциями здоровья',
                'price': 44990,
                'stock': 20
            },
            {
                'category': 'smartwatches',
                'name': 'Samsung Galaxy Watch 6',
                'slug': 'samsung-galaxy-watch-6',
                'description': 'Стильные умные часы с датчиками здоровья и длительной автономностью',
                'price': 29990,
                'stock': 18
            },
            {
                'category': 'smartwatches',
                'name': 'Garmin Fenix 7',
                'slug': 'garmin-fenix-7',
                'description': 'Спортивные часы премиум-класса с GPS и множеством режимов тренировок',
                'price': 69990,
                'stock': 10
            },
            {
                'category': 'smartwatches',
                'name': 'Xiaomi Watch 2 Pro',
                'slug': 'xiaomi-watch-2-pro',
                'description': 'Умные часы с AMOLED дисплеем, GPS и 14 днями автономности',
                'price': 19990,
                'stock': 25
            },
        ]

        for prod_data in products_data:
            category = categories[prod_data['category']]
            prod, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults={
                    'category': category,
                    'name': prod_data['name'],
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock': prod_data['stock'],
                    'available': True
                }
            )
            status = 'создан' if created else 'уже существует'
            self.stdout.write(f'Товар "{prod.name}" {status}')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))