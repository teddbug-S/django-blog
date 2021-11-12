from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms

from .models import Profile, Connected


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__()

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'display_picture']


class ConnectedUpdateForm(forms.ModelForm):

    facebook = forms.URLField(required=False, widget=forms.URLInput(
        {'placeholder': 'e.g https://facebook.com/your_fb_name'}))
    
    class Meta:
        model = Connected
        fields = ['facebook', 'instagram', 'twitter', 'github', 'youtube']
    


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']