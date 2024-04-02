from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages
from .models import Product,Category



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

