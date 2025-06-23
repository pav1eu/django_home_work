from .models import Product


class ProductService:

    @staticmethod
    def get_products_by_category(category_id):
        return Product.objects.filter(category__id=category_id,)
