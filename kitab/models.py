from django.db import models
from django.urls import reverse

class Kitab(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.title
    
    def get_absolute_name(self):
        return reverse('kitab_detail', args=[str(self.slug)])
    
    