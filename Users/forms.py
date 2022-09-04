from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-inp'}),label="Имя пользователя")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-inp'}),label="Электронная почта")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-inp'}),label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-inp'}),label="Повторный пароль")
    class Meta:    
        model = get_user_model()
        fields = ("username","email",'password1','password2')

class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-inp'}),label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-inp'}),label="Пароль")
    class Meta:
        model = get_user_model()
        fields = ("username","password")

class ChangeIMGForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("image",)

class ResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-inp'}),label="Электронная почта")
    class Meta:
        model = get_user_model()
        fields = ('email',)

class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-inp'}),label='Новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-inp'}),label="Повторный пароль")
    class Meta:
        model = get_user_model()
        fields = ('new_password1','new_password2')