from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from myApps.models import Product
from myApps.my_form import ProductForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    # for product in products:
    #     print(product.name, product.price)
    return render(request, 'home.html', {"products": products})

@login_required
def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.name}" 'Product added successfully')
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add.html', {'form': form})

# Product.objects.create(name="Unga",
    #                        code="0013992021",
    #                        price=20.00,
    #                        cost=12.33,
    #                        category="Foods",
    #                        for_sale=True
    #
#
#
#               )
@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, f"{product.name}" 'Product deleted successfully')
    return redirect('home')

@login_required
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            messages.success(request, f"{product.name}" 'Product updated successfully')
            return redirect('home')
    else:
        form = ProductForm(instance = product)
    return render(request, 'edit.html', {'form': form})

# def detail_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, "details.html", {"product": product})

@login_required
def details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "details.html", {"product": product})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Successfully  account is logged in")
            return redirect('home')
        else:
            form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    return None

@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')