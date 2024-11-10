from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from . models import *
from . token import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products":products})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        
        # if len(password) < 6:
        #     messages.warning(request, 'Password is too short!')
        #     return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('register')
        
        if password != password2:
            messages.warning(request, "Password Not Matching!")
            return redirect('register')
        
        user = User.objects.create_user(username=email, password=password)
        user.is_active =True
        user.save()
        return redirect('login')
        # send_activation_email(request, user)
        
    return render(request, 'accounts/register.html')

def send_activation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Activate You account'
    message_body = render_to_string('accounts/activation_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })
    

    email=EmailMessage(subject=subject, body=message_body, from_email=settings.EMAIL_FROM_USER,
                 to=[user.email])
    email.send()
    print(email)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
        if user is not None and generate_token.check_token(user, token):
            user.is_active =True
            user.save()
            return HttpResponse('Activated Successfully!')
        else:
            return HttpResponse('Activation link is invalid')
            

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Email or Password incorrect!')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required
def signout(request):
    logout(request)
    return redirect('login')
@login_required
def profile(request):
    return render(request, "accounts/profile.html")

def products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {"products":products})


def order(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        state = request.POST['state']
        town = request.POST['town']
        email = request.POST['email']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        
        order_address = OrderAddress.objects.create(
            first_name=fname,
            last_name=lname, 
            address=address,
            state = state,
            town =town,
            email = email,
            phone1 = phone1,
            phone2 = phone2
            )
        
        order_address.save()
        return redirect('summary')
    return render(request, "order.html")


def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    cart, created =Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        
        cart.save()
        return redirect("products")
    
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

def get_cart_count(request):
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    return {'cart_count': cart_count}
    

def view_cart(request):
    cart = Cart.objects.get(user=request.user)  # Assuming each user has one cart
    cart_items = cart.items.all()  # Or wherever the items are stored within the cart
    total = sum(item.product.price * item.quantity for item in cart_items)# Calculate total
    return render(request, "cart.html", {"cart_items": cart_items, "total": total})

def search(request):
    query = request.GET.get('query', None)
    results = []
    if query:
        results = Product.objects.filter(name_icontains=query) | Product.objects.filter(desc_icontains=query)
          
    return render(request, 'search.html', {'query': query, 'results': results})

def order_summary(request):
    address = OrderAddress.objects.filter(user=request.user).last()
    
    if OrderAddress.objects.filter(user=request.user).exists():
        return redirect('payment')
    
    return render(request, 'order_summary.html', {'address': address})

def payment_page(request):
    return render(request, 'payment.html')
    
    
        