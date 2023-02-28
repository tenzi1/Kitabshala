from django.contrib import admin

from .models import Kitab

@admin.register(Kitab)
class KitabAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'slug')
    prepopulated_fields ={'slug':('title',)}