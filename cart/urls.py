# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
    # ADD THESE:
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<int:order_id>/simulation/', views.payment_simulation, name='payment_simulation'),
    path('order/<int:order_id>/confirmed/', views.order_confirmed, name='order_confirmed'),
    path('my-orders/', views.my_orders, name='my_orders'),
]