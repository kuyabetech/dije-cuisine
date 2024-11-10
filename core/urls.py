from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('activate/<uid64>/<token>', activate, name='activate'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('profile/', profile, name='profile'),
    path('products/', products, name='products'),
    path('order/', order, name='order'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('search/', search, name='search'),
    path('summary/', order_summary, name='summary'),
    path('payment/', payment_page, name='payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)