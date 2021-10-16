from django import forms
from .models import OrderItem, VarietySpec, Product


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