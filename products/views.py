from django.shortcuts import render
from .models import Product
from django.db.models import Q # This allows us to search both Name AND Description

def product_list(request):
    query = request.GET.get('q') # Get the text from the search bar
    
    if query:
        # This filters the products where the name or description contains the search text
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        # If no search, show everything as usual
        products = Product.objects.all()
        
    return render(request, 'products/index.html', {'products': products})
from django.shortcuts import render, get_object_or_404 # Add get_object_or_404 to your imports
from .models import Product

# ... (keep your existing product_list view) ...

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Grab 3 other products, excluding the one the user is currently looking at
    related_products = Product.objects.exclude(pk=pk)[:3] 
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products # Pass this to the template
    })
def product_list(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category') # New line
    
    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category_filter:
        products = products.filter(category=category_filter) # Filter by category

    return render(request, 'products/index.html', {
        'products': products,
        'categories': ['Keyboard', 'Mouse', 'Monitor'] # Pass category list to template
    })
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # NEW LOGIC: Get 3 related products from the same category
    # .exclude(id=pk) makes sure we don't show the product we are currently viewing
    related_products = Product.objects.filter(category=product.category).exclude(id=pk)[:3]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)