from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from user.models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):

    username = forms.CharField(help_text=None,
                              label=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    full_name = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    email = forms.EmailField(label=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    password1 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def save_superuser(self):
        user = self.save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    
    password = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.PasswordInput(attrs={'placeholder' : 'Contraseña'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=None,
                               label="Nombre de usuario")
    
    full_name = forms.CharField(help_text=None,
                                label="Nombre completo")
    
    email = forms.EmailField(label="Correo")

    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(label="Foto",
                             help_text=None,
                             required=False,
                             widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = [
            'photo',
        ]

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    new_password1 = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))
    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]