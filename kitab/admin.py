from django.contrib import admin

from .models import Kitab, Category, Author

@admin.register(Kitab)
class KitabAdmin(admin.ModelAdmin):
    list_display = ('title',  'price', 'slug')
    prepopulated_fields ={'slug':('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name')
   