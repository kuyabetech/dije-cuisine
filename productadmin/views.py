from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import StaffRegistrationFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.models import *

# Create your views here.

@login_required(login_url='/staff')
def dashboard(request):
    return render(request, 'dije-admin/dashoard.html')

def register(request):
    if request.method == 'POST':
        form = StaffRegistrationFrom(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
        
    else:
        form = StaffRegistrationFrom()
    return render(request, 'dije-admin/register.html', {'form': form})

def staff(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dije-admin/login.html')

@login_required(login_url='/staff')
def signout(request):
    logout(request)
    return redirect('staff')

@login_required(login_url='/staff')
def add_product(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        image = request.POST.get('image')
        price = request.POST.get('price')
        created = request.POST.get('created')
        
        products = Product.objects.create(
            name=name,
            desc = desc,
            category = category,
            image = image,
            price = price,
            created_at = created
        )
        
        products.save()
        return redirect('product')
        
        
    return render(request, 'dije-admin/add-product.html', {'categories':categories, 'product': product})

@login_required(login_url='/staff')
def edit_product(request):
    return render(request, 'dije-admin/edit-product.html')

@login_required(login_url='/staff')
def account(request):
    users = User.objects.all()
    return render(request, 'dije-admin/accounts.html', {'users':users})

@login_required(login_url='/staff')
def product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'dije-admin/products.html', context)

@login_required(login_url='/staff')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('account')
    
    return render(request, 'dije-admin/confirm_delete.html', {'user':user})
@login_required(login_url='/staff')
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product')
    
    return render(request, 'dije-admin/product_delete_confirm.html', {'product':product})

@login_required(login_url='/staff')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('product')
    
    return render(request, 'dije-admin/category_delete_confirm.html', {'category':category})

def add_category(request):
    
    if request.method ==  'POST':
        name = request.POST.get('name')
        
        category = Category.objects.create(name=name)
        category.save()
        return redirect('product')
    
    return render(request, 'dije-admin/add-category.html')