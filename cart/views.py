# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from products.models import Product
from .forms import OrderCreateForm
from django.contrib.auth.decorators import login_required

# --- Cart Management Functions ---
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    if str(product_id) not in cart:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }
    else:
        cart[str(product_id)]['quantity'] += 1
        
    request.session['cart'] = cart
    return redirect('cart:view_cart')

def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    action = request.GET.get('action')
    
    if str(product_id) in cart:
        if action == 'increase':
            cart[str(product_id)]['quantity'] += 1
        elif action == 'decrease':
            cart[str(product_id)]['quantity'] -= 1
            if cart[str(product_id)]['quantity'] <= 0:
                del cart[str(product_id)]
                
    request.session['cart'] = cart
    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    total = 0
    for item in cart.values():
        if isinstance(item, dict):
            total += item['price'] * item['quantity']
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'total': total})

# --- Checkout and Payment Functions ---
@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    
    # Calculate total based on the current session cart
    total = sum(float(item['price']) * item['quantity'] for item in cart.values() if isinstance(item, dict))

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # 1. Create the Order
            order = form.save(commit=False)
            order.user = request.user
            # Capture the manual name from the input field
            order.full_name = request.POST.get('full_name', request.user.username)
            order.total_price = total
            order.status = 'Pending' # Explicitly set to Pending
            order.save()
            
            # 2. Create Order Items from cart
            for product_id, item in cart.items():
                if isinstance(item, dict):
                    OrderItem.objects.create(
                        order=order,
                        product_id=product_id,
                        price=item['price'],
                        quantity=item['quantity']
                    )
            
            # 3. Clear the Cart
            request.session['cart'] = {}
            
            # 4. Handle Payment Method redirection
            if order.payment_method == 'SIM':
                return redirect('cart:payment_simulation', order_id=order.id)
            else:
                return redirect('cart:order_confirmed', order_id=order.id)
    else:
        # GET request: provide an empty form
        form = OrderCreateForm()
    
    # CRITICAL: This return must be here for GET requests and invalid POSTS
    return render(request, 'cart/checkout.html', {
        'cart': cart, 
        'total': total, 
        'form': form
    })

@login_required
def payment_simulation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'cart/payment_simulation.html', {'order': order})

@login_required
def order_confirmed(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'cart/order_confirmed.html', {'order': order})
# cart/views.py

# cart/views.py

@login_required
def payment_simulation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        # This is where you'd normally integrate a real API. 
        # For our demo, we just assume success and redirect.
        return redirect('cart:order_confirmed', order_id=order.id)
        
    return render(request, 'cart/payment_simulation.html', {'order': order})
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'cart/my_orders.html', {'orders': orders})