from django.db import models

# Create your models here.
class Menu(models.Model):
    TYPES = [('veg', 'Veg'), ('non_veg', 'NonVeg')]
    item = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category = models.ManyToManyField('category', related_name='item', blank=True, null=True)
    veg_or_nonveg = models.CharField(max_length=10, choices=TYPES)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.item}'
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'