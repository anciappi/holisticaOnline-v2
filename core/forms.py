from django import forms
from accounts.models import Profile
from .models import Terapias
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# FORM - LOGIN
class LoginForm(AuthenticationForm):
    pass

# FORM - REGISTRO
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    #Validacion de email
    def clean_email(self):
        email_field = self.cleaned_data['email']

        if User.objects.filter(email = email_field).exists():
            raise forms.ValidationError('El email ya se encuentra registrado')
        
        return email_field
    

# FORM - EDICION DE PERFIL
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'country', 'city', 'phone', 'instagram', 'facebook', 'twitter', 'description', 'titulo')


class TerapiasForms(forms.ModelForm):
    class Meta:
        model = Terapias
        fields = ('title', 'subtitle', 'description', 'image')