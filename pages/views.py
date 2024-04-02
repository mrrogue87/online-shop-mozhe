from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from products.models import Category,Product
from django.views import generic



class HomePageDetailView(generic.DetailView):
    model = Product
    template_name = "pages/home_page.html"
    context_object_name = 'proudct'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryes'] = Category.objects.all()
        return context

    def get_object(self, ) :
        proudct_discount = Product.objects.filter(discount__isnull=False)
        proudct_popularity = Product.objects.filter(popularity=True)
        proudct_all = Product.objects.filter(active=True)
        
        return {
            'proudct_discount':proudct_discount,
            'proudct_popularity':proudct_popularity,
            'proudct_all':proudct_all
        }
        
    
    
    

class CategoryListView(generic.ListView):
        model = Category
        template_name = "pages/category_list.html"
        context_object_name = 'category'
        
        def get_queryset(self, **kwargs) :
            category_id = self.kwargs.get('pk')
            return Product.objects.filter(category=category_id)