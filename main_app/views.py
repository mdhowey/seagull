from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class ProductsList(TemplateView):
    template_name = "products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["products"] = Product.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["products"] = Product.objects.all()
            # default header for not searching 
            context["header"] = "Trending products"
        return context

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'img', 'price', 'category', 'description']
    template_name = "product_create.html"
    success_url = "/products/"

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'img', 'price', 'category', 'description']
    template_name = 'product_update.html'
    success_url = '/products/'

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = '/products/'