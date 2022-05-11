from django.contrib import admin
# мои импорты
from .models import *

# регистрация таблиц в админ панель
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Product)
