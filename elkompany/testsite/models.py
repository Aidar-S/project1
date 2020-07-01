from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,
                            default="",
                            verbose_name="Название", )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tovar(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 default=1,
                                 verbose_name="Категория", )

    name = models.CharField(max_length=100,
                            default="",
                            verbose_name="Название", )
    desc = models.TextField(default="",
                            verbose_name="Описание", )
    price = models.FloatField(verbose_name="Цена", )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
