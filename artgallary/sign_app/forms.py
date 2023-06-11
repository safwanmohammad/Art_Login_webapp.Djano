from .models import Register
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['user_name','password','email','phone_no']

         