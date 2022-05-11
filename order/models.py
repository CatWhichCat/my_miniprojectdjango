from tkinter import CASCADE
from django.db import models
# мои импорты
from main.models import Product


# моделька отвечающая за покупку
class Order(models.Model):
    categories = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name='orders') 
# за счет related_name='order' я могу через заказы обратится к определенному продукту
    phone = models.CharField(max_length=13)
    address = models.TextField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    
    
    def __str__(self):
        return f"{self.email} - {self.phone}"