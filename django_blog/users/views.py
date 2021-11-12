from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from .forms import (ConnectedUpdateForm, ProfileUpdateForm, UserLoginForm,
                    UserRegisterForm, UserUpdateForm)

# Create your views here.

class RegisterView(View):
    def get(self, request):
        """ Handles the register screen """
        form = UserRegisterForm()
        context = {'title': 'Register', 'form': form}
        return render(request, template_name='users/signup.html', context=context)

    def post(self, request):
        """ Handles the register screen """
        form = UserRegisterForm(request.POST)
        context = {'title': 'Register', 'form': form}
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('blog-home')
        return render(request, template_name='users/signup.html', context=context)


class LoginView(View):

    def login(self, **creds):
        """ Logs a user in """
        username = creds.get('username')
        password = creds.get('password')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return None
        else:
            return user

    def get(self, request):
        """ Handles the register screen """
        form = UserLoginForm()
        context = {'title': 'Login', 'form': form}
        return render(request, template_name='users/login.html', context=context)
    
    def post(self, request):
        """ Handles the login data """
        form = UserLoginForm(request.POST)
        context = {'title': 'Login', 'form': form}
        print(request.POST)
        if form.is_valid():
            user = self.login(**form.cleaned_data)
            if user:
                context['user'] = user
                return redirect('blog-home')
        return render(request, template_name='users/login.html', context=context)
            

class ProfileView(LoginRequiredMixin, View):
    """ The Profile view """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "Please login first, the page you tried to access requires you to login.")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, username):
        """ Handles every get request made to the profile page """
        # login_url = 'users/login'
        # redirect_field_name = 'next'
        user_ = User.objects.get(username=username)
        context = {'title': 'Profile', 'user_': user_}
        return render(request, template_name='users/profile.html', context=context)


class ProfileUpdateView(LoginRequiredMixin, View):
    # override the dispatch method to add an alert
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "Please login to update your profile.")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        # initialize all forms for a profile
        # setting the instance populates form with existing data
        u_form = UserUpdateForm(instance=request.user) # user object form
        c_form = ConnectedUpdateForm(instance=request.user.profile.linked_accounts) # connected accounts form
        p_form = ProfileUpdateForm(instance=request.user.profile) # profile object form
        
        context = {
            'title': 'Edit Profile',
            'u_form': u_form,
            'p_form': p_form,
            'c_form': c_form,
        }
        # render 
        return render(request, template_name='users/edit-profile.html', context=context)

    
    def post(self, request):
        # handle POST requests
        # check and save form data
        u_form = UserUpdateForm(request.POST, instance=request.user) # user object form
        c_form = ConnectedUpdateForm(request.POST, instance=request.user.profile.linked_accounts) # connected accounts form
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile) # profile object form
        # check for form validation
        if u_form.is_valid() and c_form.is_valid() and p_form.is_valid():
            u_form.save(), c_form.save(), p_form.save() # save data for each form
            # send a success message
            messages.success(request, f"Profile updated sucessfully.")
            # redirect to profile page
            return redirect('users-profile', request.user.username)
