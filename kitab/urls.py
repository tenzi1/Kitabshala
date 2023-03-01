from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("kitabs/", views.KitabListView.as_view(), name='kitab_list'),
    path("kitab/<slug:slug>/", views.KitabDetailView.as_view(), name="kitab_detail"),

    path("category/<slug:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),

]