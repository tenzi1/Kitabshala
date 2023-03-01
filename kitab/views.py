from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Kitab, Category

class HomePageView(TemplateView):
    template_name = 'home.html'
    


class KitabListView(ListView):
    model = Kitab
    template_name='kitab_list.html'

    
class KitabDetailView(DetailView):
    model = Kitab
    template_name = 'kitab_detail.html'
    context_object_name = 'kitab'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_detail.html'