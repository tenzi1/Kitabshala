from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class HomePageView(TemplateView):
    template_name = 'home.html'


class KitabListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'kitab_list.html')