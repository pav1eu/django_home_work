from django.urls import path
from catalog.views import home, contacts, products_list, product_detail, description

app_name = 'catalog'


urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", products_list, name="products_list"),
    path("product_detail/<int:product_id>/", product_detail, name="product_detail"),
    path("description/", description, name="description"),
]