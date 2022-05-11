from django.urls import path
# мои импорты
from main.views import index


urlpatterns = [
    path('', index)
]
