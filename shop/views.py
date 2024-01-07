from django.shortcuts import redirect, render
from django.contrib import messages
from . models import Category, Product

# Create your views here.

def home(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'shop/index.html', context)


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'shop/collections.html', context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'shop/products/index.html', context)
    else:
        messages.warning(request, 'No such category found')
        return redirect('collections')   

def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):

        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, 'No such product found')
            return redirect('collections') 

    else:
        messages.error(request, 'No such category found')
        return redirect('collections')
    return render (request, 'shop/products/view.html', context) 
