from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('staff/', staff, name='staff'),
    path('admin-register/', register, name='register'),
    path('product/', product, name='product'),
    path('account/', account, name='account'),
    path('add-product/', add_product, name='add-product'),
    path('add-category/', add_category, name='add-category'),
    path('edit-product/', edit_product, name='edit-product'),
    path('logout/', signout, name='logout'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('delete_product/<int:product_id>/', delete_product , name='delete_product'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
]
