from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
from django.http import HttpResponse


def index(request):
    all_prods = []
    catprods = Product.objects.values('category', 'id')
    catgs = {item['category'] for item in catprods}
    for catg in catgs:
        prod = Product.objects.filter(category=catg)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        all_prods.append([prod, range(1,  nSlides), nSlides])
        params = {'all_prods': all_prods}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def productView(request):
    return HttpResponse("We are at product view")


def checkout(request):
    return HttpResponse("We are at checkout")


