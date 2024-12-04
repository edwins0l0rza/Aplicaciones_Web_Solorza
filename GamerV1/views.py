from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Producto
from GamerV1.forms import ProductoForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crea_producto.html'
    success_url = '/productos/'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'editar_producto.html'
    success_url = '/productos/'

class ProductoDeleteView(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'eliminar_producto.html'
    success_url = '/productos/'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'ver_producto.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    succes_url = reverse_lazy('home')
