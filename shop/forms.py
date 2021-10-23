from django.contrib.auth import get_user_model
from django import forms
from .models import OrderItem, VarietySpec, Product, Address

User = get_user_model()

class AddToCartForm(forms.ModelForm):

    variety = forms.ModelChoiceField(queryset=VarietySpec.objects.none())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = OrderItemfields = ['quantity', 'variety']

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)

        self.fields['variety'].queryset = product.available_varieties.all()

    def clean(self):
        product_id = self.product_id
        product = Product.objects.get(id=self.product_id)
        quantity = self.cleaned_data['quantity']
        max_available = product.stock - 5
        if max_available < 0:
            print_max = 0
        else:
            print_max = max_available    

        if max_available < quantity:
            raise forms.ValidationError(f"Sorry, the most we can accept an order for at the moment is {print_max}. Please adjust your order.")
            



class AddressForm(forms.Form):
    
    shipping_address_line_1 = forms.CharField(required=False)
    shipping_address_line_2 = forms.CharField(required=False)
    shipping_address_county = forms.CharField(required=False)
    shipping_address_eircode = forms.CharField(required=False)

    billing_address_line_1 = forms.CharField(required=False)
    billing_address_line_2 = forms.CharField(required=False)
    billing_address_county = forms.CharField(required=False)
    billing_address_eircode = forms.CharField(required=False)

    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required = False
    )
    selected_billing_address = forms.ModelChoiceField(
        Address.objects.none(), required = False
    )

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user=User.objects.get(id=user_id)

        shipping_address_queryset = Address.objects.filter(
        user=user,
        address_type='S',
        )
        billing_address_queryset = Address.objects.filter(
        user=user,
        address_type='B',
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_queryset
        self.fields['selected_billing_address'].queryset = billing_address_queryset

    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_line_1', None):
                self.add_error("shipping_address_line_1", "Fill in this field")
            if not data.get('shipping_address_line_2', None):
                self.add_error("shipping_address_line_2", "Fill in this field")
            if not data.get('shipping_address_county', None):
                self.add_error("shipping_address_county", "Fill in this field")
            if not data.get('shipping_address_eircode', None):
                self.add_error("shipping_address_eircode", "Fill in this field")

        selected_billing_address = data.get('selected_shipping_address', None)
        if selected_billing_address is None:
            if not data.get('billing_address_line_1', None):
                self.add_error("billing_address_line_1", "Fill in this field")
            if not data.get('billing_address_line_2', None):
                self.add_error("billing_address_line_2", "Fill in this field")
            if not data.get('billing_address_county', None):
                self.add_error("billing_address_county", "Fill in this field")
            if not data.get('billing_address_eircode', None):
                self.add_error("billing_address_eircode", "Fill in this field")


class StripePaymentForm(forms.Form):
    selectedCard = forms.CharField(max_length=100)
