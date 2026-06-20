from django.contrib import admin
from .models import Order, OrderItem

# --- CUSTOMIZE EZ SPORTZ ADMIN INTERFACE ---
# Renaming the "Hive" to the "Arena" or "Command Center"
admin.site.site_header = "EZ SPORTZ | Command Center"
admin.site.site_title = "Ez Sportz Elite Admin"
admin.site.index_title = "Locker Room & Order Management"

class OrderItemInline(admin.TabularInline):
    """
    Shows the gear items inside the order view
    """
    model = OrderItem
    extra = 0
    # Keep readonly to prevent accidental price/product tampering after purchase
    readonly_fields = ['product', 'price', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Professional list view for quick status checks
    list_display = ['id', 'user', 'full_name', 'total_price', 'status', 'created']
    
    # Filter by 'status' to quickly find 'Pending' or 'Shipped' gear
    list_filter = ['status', 'created']
    
    # Allows the admin to change status (e.g., Shipped) directly from the list
    list_editable = ['status'] 
    
    # Search by Order ID, Customer Name, or Email
    search_fields = ['id', 'full_name', 'user__email']
    
    # Displays the specific items (jerseys, cleats, etc.) inside the order detail
    inlines = [OrderItemInline]
    
    # Link to custom CSS for those Ez Sportz red/dark status badges
    class Media:
        css = {
            'all': ('admin/css/ez_sportz_admin.css',)
        }