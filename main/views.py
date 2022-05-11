from django.shortcuts import render

# мои импорты
from main.models import Product, Category

# страничка в которой представленны все блюда
def index(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'category': categories})