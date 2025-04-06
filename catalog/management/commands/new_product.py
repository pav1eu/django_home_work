from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="Овощ", description="Вкусно и полезно"
        )

        products = [
            {
                "name": "Огурец",
                "description": "Зеленый",
                "category": category,
                "price": 50,
            },
            {
                "name": "Помидор",
                "description": "Красный",
                "category": category,
                "price": 40,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exist: {product.name}")
                )
