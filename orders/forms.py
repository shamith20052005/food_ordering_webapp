from django import forms
from orders.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean_address(self):
        address = self.cleaned_data['address']
        user = self.request.user

        if Address.objects.filter(user=user, address=address).exists():
            raise forms.ValidationError('This address already exists for your account.')

        return address