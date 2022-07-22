from typing import List
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from Posts.models import UserProfile

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
	    return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password-changed')

def ChangedPasswordView(request):
    return render(request, 'registration/changed-password.html', {})

class ShowProfileView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = UserProfile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['user'] = user
        return context 
    
class EditProfileView(generic.UpdateView):
    model = UserProfile
    template_name='registration/edit_profile_page.html'
