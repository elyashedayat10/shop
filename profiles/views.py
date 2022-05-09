from django.views.generic import UpdateView
from .models import Profile
from .mixins import OwnerMixin
from django.urls import reverse
from .forms import ProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class ProfileUpdateView(OwnerMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/update.html'
    slug_field = 'id'
    slug_url_kwarg = 'profile_id'
    success_message = ''

    def get_success_url(self):
        return reverse('accounts:dashboard')

    def form_invalid(self, form):
        messages.error(self.request, '', 'danger')
        return super(ProfileUpdateView, self).form_invalid(form)
