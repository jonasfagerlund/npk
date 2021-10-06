from django.db import models
from django.views.generic import ListView

from .models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product_list.html'
