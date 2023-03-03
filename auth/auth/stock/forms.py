from django import forms  
from stock.models import Stock  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StockForm(forms.ModelForm):  
    class Meta:  
        model = Stock  
        fields = "__all__"  
        exclude=('user',)  


class UserRegistrationForm(UserCreationForm):
    # choice=forms.CharField(label='Who are you ?',widget=forms.RadioSelect(choices=TYPE))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email','password1', 'password2']  