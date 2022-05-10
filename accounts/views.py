from random import randint

from braces.views import AnonymousRequiredMixin, SuperuserRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, View

from .forms import OtpCodeForm, AuthForm, AdminForm
from .mixins import AdminMixin
from .models import OtpCode
from .utils import send_otp

user = get_user_model()


class UserAuthView(AnonymousRequiredMixin, View):
    template_name = "accounts/auth.html"
    form_class = AuthForm
    authenticated_redirect_url = reverse_lazy("account:dashboard")

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = randint(000000, 999999)
            phone_number = form.cleaned_data["phone_number"]
            send_otp(phone_number, code)
            OtpCode.objects.create(phone_number=phone_number, code=code)
            request.session["user_info"] = {
                "phone_number": form.cleaned_data["phone_number"],
            }
            messages.success(request, "code sent", "success")
            return redirect()
        messages.error(request, "error", "danger")
        return render(request, self.template_name, {"form": form})


class UserVerifyView(AnonymousRequiredMixin, View):
    template_name = "accounts/verify.html"
    form_class = OtpCodeForm
    authenticated_redirect_url = reverse_lazy("account:dashboard")

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        user_session = request.session["user_info"]["phone_number"]
        code_instance = OtpCode.objects.get(phone_number=user_session)
        if form.is_valid():
            code = form.cleaned_data["code"]
            if code == code_instance:
                code_instance.delete()
                user_obj = user.objects.filter(phone_number=user_session)
                if user_obj.exists():
                    login(request, user_obj)
                else:
                    user.objects.create_user(phone_number=user_session)
                messages.success(request, "", "")
                return redirect("")
        messages.error(request, "", "")
        return render(request, self.template_name, {"form": self.form_class})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "", "success")
        return redirect()


class UserDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        user_obj = get_object_or_404(user, id=self.request.user)
        return render(request, "accounts/dashboard.html", {"user": user_obj})


class AdminUserListView(SuperuserRequiredMixin, ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = "accounts/admin_list.html"


class UserListView(AdminMixin, ListView):
    queryset = user.objects.exclude(is_admin=True)
    template_name = "accounts/user_list.html"


class AdminUserCreateView(SuperuserRequiredMixin, View):
    template_name = "accounts/admin_create.html"
    form_class = AdminForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user.objects.create_admin_user(
                phone_number=cd["phone_number"], password=cd["password"]
            )
            messages.success(request, "", "success")
            return redirect("")
        else:
            messages.error(request, "", "danger")
        return render(request, self.template_name, {"form": form})


class UserDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, user_id):
        user_obj = get_object_or_404(user, id=user_id)
        user_obj.delete()
        messages.success(request, "", "success")
        return redirect()
