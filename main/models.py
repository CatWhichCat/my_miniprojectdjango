from tkinter import CASCADE
from django.db import models

# Автор
class Author(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=85, blank=True)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='authors')
    
    # этот метод отвечает за название автора(продукта, категории) в адм.Панели
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
# моделька создающая категории 
class Category(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)
    
    def __str__(self):
        return self.name
        
# моделька создающая продукты
class Product(models.Model):
    # функция отвечающая за выборку!
    CHOICES = (
        ('in stock', 'В наличии'), ('out of stock', 'Нет в наличии'),
    )
    
    title = models.CharField(max_length=55, )
    image = models.ImageField(blank=True, null=True, unique='products')
    status = models.CharField(choices=CHOICES, max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, 
                               related_name='products')
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title