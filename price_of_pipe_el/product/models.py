from django.db import models


class Product(models.Model):
    category = models.CharField(verbose_name='Категория')
    designation = models.CharField(verbose_name='Обозначение/Артикуль')
    diameter_dn = models.IntegerField(verbose_name='Условный проход')
    pressure_pn = models.IntegerField(verbose_name='Условное давление')
    material = models.CharField(verbose_name='Материал')
    price = models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name = ('Изделие')
        verbose_name_plural = ('Изделия')
