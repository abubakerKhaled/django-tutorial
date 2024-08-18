from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Customer

# ... Your existing RegisterForm and LoginForm ...


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "company",
            "job",
            "country",
            "address",
            "phone",
            "email",
            "facebook_url",
            "linkedin_url",
            "instagram_url",
            "x_url",
            "profile_image",
        ]


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "company",
            "job",
            "country",
            "address",
            "phone",
            "email",
            "facebook_url",
            "linkedin_url",
            "instagram_url",
            "x_url",
            "profile_image",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "job": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "facebook_url": forms.URLInput(attrs={"class": "form-control"}),
            "linkedin_url": forms.URLInput(attrs={"class": "form-control"}),
            "instagram_url": forms.URLInput(attrs={"class": "form-control"}),
            "x_url": forms.URLInput(attrs={"class": "form-control"}),
            "profile_image": forms.FileInput(attrs={"class": "form-control-file"}),
        }

class CustomerPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'id': 'currentPassword'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'id': 'newPassword'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'id': 'renewPassword'})