from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Kitab(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    synapsis = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('kitab_detail', args=[str(self.slug)])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
 