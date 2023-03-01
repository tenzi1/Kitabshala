from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.db.models import Q

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


class FilterSearchView(ListView):
    model = Kitab
    context_object_name = "kitab_list"
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        result = Kitab.objects.filter(
            Q(title__icontains='think') | Q(authors__full_name__icontains=query)
        ).distinct()
        print(result)
        return  result


        

