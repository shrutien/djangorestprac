from django import forms

from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Enter Email')
    first_name = forms.CharField(label='Full Name')

    class Meta:
        model = User
        fields=['username','email','first_name','password1','password2']


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')        

        if password1 and password2 and password1 != password2:            
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user