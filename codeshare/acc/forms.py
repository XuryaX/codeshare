__author__ = 'Shaurya'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields =('username','email','password1','password2')

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The Username is already in use. Please Choose Another")


    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("The Email is already in use. Please Choose Another")

    def clean_password2(self):
        if self.cleaned_data['password1']!=self.cleaned_data['password2']:
              raise forms.ValidationError("The two passwords should match")
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            raise forms.ValidationError("The Username does  not exist")
        return self.cleaned_data['username']