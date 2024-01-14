from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from .forms import UserForm, ProfileForms
from accounts.models import Profile
from .models import Terapias

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    
class AboutView(TemplateView):
    template_name = 'core/about.html'
    

class TerapiasListView(ListView):
    model = Terapias
    template_name = 'core/terapias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    

class TerapeutasListView(ListView):
    model = Profile
    template_name = 'core/terapeutas.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context



# REGISTER
class RegisterView(View):
    
    def get(self, request):
        data = {
            'form': RegisterForm()
        }

        return render(request, 'core/registration/register.html', data)
    
    def post(self,request):
        user_creation_form = RegisterForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
        data = {
            'form': user_creation_form
        }
        return render(request, 'registration/login.html')
    

# PROFILE VIEW
class ProfileView(TemplateView):
    template_name = 'core/profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_form'] = UserForm(instance=user)
        context['profile_form'] = ProfileForms(instance=user.profile)
        return context


    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForms(request.POST, request.FILES, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'core/profile/profile.html', context)