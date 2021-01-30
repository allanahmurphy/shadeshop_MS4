from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Brand
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['brand'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    # Ensure Sale Items have sale price
    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        sale = cleaned_data.get("sale")
        saleprice = cleaned_data.get("saleprice")

        if sale and saleprice is None:
            msg = "Sale items must have sale price"
            self.add_error('saleprice', msg)