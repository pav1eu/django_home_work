from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание продукта"
    )
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория продукта",
    )
    price = models.IntegerField(null=True, blank=True, verbose_name="Цена")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата производства"
    )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.category} {self.name} {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание категории"
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
