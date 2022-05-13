from random import randint

from braces.views import AnonymousRequiredMixin, SuperuserRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, View

from .forms import AuthForm, OtpCodeForm
from .mixins import AdminMixin
from .models import OtpCode
from .utils import send_otp

user = get_user_model()


class UserAuthView(AnonymousRequiredMixin, FormView):
    template_name = "accounts/auth.html"
    form_class = AuthForm
    success_url = reverse_lazy("account:verify")

    def get_form_kwargs(self):
        kwargs = super(UserAuthView, self).get_form_kwargs()
        kwargs["user_auth"] = True
        return kwargs

    def form_valid(self, form):
        code = randint(000000, 999999)
        phone_number = form.cleaned_data["phone_number"]
        send_otp(phone_number, code)
        OtpCode.objects.create(phone_number=phone_number, code=code)
        self.request.session["user_info"] = {
            "phone_number": form.cleaned_data["phone_number"],
        }
        messages.success(self.request, "code sent", "success")
        return super(UserAuthView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "error", "danger")
        return super(UserAuthView, self).form_invalid(form)


class UserVerifyView(AnonymousRequiredMixin, FormView):
    template_name = "accounts/verify.html"
    form_class = OtpCodeForm
    authenticated_redirect_url = reverse_lazy("account:dashboard")

    def dispatch(self, request, *args, **kwargs):
        if self.request.META.get("HTTP_REFERER") == "":
            return super(UserVerifyView, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def form_valid(self, form):
        user_session = self.request.session["user_info"]["phone_number"]
        code_instance = OtpCode.objects.get(phone_number=user_session)
        code = form.cleaned_data["code"]
        if code == code_instance:
            code_instance.delete()
            user_obj = user.objects.filter(phone_number=user_session)
            if user_obj.exists():
                login(self.request, user_obj)
            else:
                user.objects.create_user(phone_number=user_session)
            messages.success(self.request, "", "")
        return super(UserVerifyView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "")
        return super(UserVerifyView, self).form_invalid(form)


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "", "success")
        return redirect("account:auth")


class UserDashboardView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        print(request.user.id)
        user_obj = get_object_or_404(user, id=user_id)
        return render(request, "accounts/dashboard.html", {"user": user_obj})


class AdminUserListView(SuperuserRequiredMixin, ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = "accounts/admin_list.html"
    context_object_name = 'admin_list'


class UserListView(AdminMixin, ListView):
    queryset = user.objects.exclude(is_admin=True)
    template_name = "accounts/user_list.html"
    context_object_name = 'user_list'


class AdminUserCreateView(SuperuserRequiredMixin, FormView):
    redirect_unauthenticated_users = reverse_lazy("account:auth")
    template_name = "accounts/admin_create.html"
    form_class = AuthForm

    def form_valid(self, form):
        cd = form.cleaned_data
        user.objects.create_admin_user(
            phone_number=cd["phone_number"],
            password=cd["password"],
        )
        messages.success(self.request, "", "success")
        return super(AdminUserCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "danger")
        return super(AdminUserCreateView, self).form_invalid(form)


class UserDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, user_id):
        user_obj = get_object_or_404(user, id=user_id)
        user_obj.delete()
        messages.success(request, "", "success")
        return redirect("account:admin_list")
