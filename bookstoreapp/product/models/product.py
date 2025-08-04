#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models

from product.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        app_label = 'product'


    def __str__(self):
        return self.title
      
