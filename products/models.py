from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    
    def __str__(self) :
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(null=True,blank=True)
    active = models.BooleanField(default=True)
    popularity = models.BooleanField(default=False)
    # image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(_('Date Time of Creation'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


