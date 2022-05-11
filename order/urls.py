from django.urls import path
# Мои импорты
from order.views import order

urlpatterns = [
    path('', order)
]
