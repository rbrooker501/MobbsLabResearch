"""
Loads the relevant views for the page that the user is on.
"""

from typing import List
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm, CreateProfilePageForm
from Posts.models import UserProfile

class UserRegisterView(generic.CreateView):
    """Creates the view for a user to register using the
    SignUpForm."""
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    """Creates the view for a user to edit their info using
    the EditProfileForm."""
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
	    return self.request.user

class ChangePasswordView(PasswordChangeView):
    """Creates the view for a user to change their password
    using the ChangePasswordForm"""
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password-changed')

def ChangedPasswordView(request):
    """Redirects the user to a success page upon changing their password"""
    return render(request, 'registration/changed-password.html', {})

class ShowProfileView(DetailView):
    """Creates the view to show the user a profile page"""
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # Gets the right profile page for the user to see
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['user'] = user
        return context 
    
class EditProfileView(generic.UpdateView):
    """Creates the view for a user to edit their profile page"""
    model = UserProfile
    template_name='registration/edit_profile_page.html'
    fields = ['bio', 'profile_picture']
    success_url = reverse_lazy('home')

class CreateProfileView(CreateView):
    """Creates the view for a user to create their profile page
    using the CreateProfilePageForm."""
    model = UserProfile
    form_class = CreateProfilePageForm
    template_name='registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)