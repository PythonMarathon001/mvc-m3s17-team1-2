from django import forms
from .models import Order


class OrderForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Order
        fields = ('user', 'book')
        labels = {
            'user': 'Name of User',
            'book': 'Available books',
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        self.fields['book'].required = False
