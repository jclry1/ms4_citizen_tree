from django.contrib.auth import get_user_model
from django import forms
from .models import OrderItem, VarietySpec, Product, Address

User = get_user_model()

class AddToCartForm(forms.ModelForm):

    variety = forms.ModelChoiceField(queryset=VarietySpec.objects.none())

    class Meta:
        model = OrderItem
        fields = OrderItemfields = ['quantity', 'variety']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)
        super().__init__(*args, **kwargs)

        self.fields['variety'].queryset = product.available_varieties.all()


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