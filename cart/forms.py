# cart/forms.py
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'payment_method']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address, Kathmandu'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'payment_method': 'Payment Method',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # CHANGE THIS LINE
        self.fields['payment_method'].choices = [
            ('COD', 'Cash on Delivery'),
            ('SIM', 'Online Payment'), # Renamed here
        ]