from django.urls import path

from .views import (
    AdminUserCreateView,
    AdminUserListView,
    UserAuthView,
    UserDashboardView,
    UserDeleteView,
    UserListView,
    UserLogoutView,
    UserVerifyView,
)

app_name = "account"
urlpatterns = [
    path("auth/", UserAuthView.as_view(), name="auth"),
    path("verify/", UserVerifyView.as_view(), name="verify"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("dashboard/<int:user_id>/", UserDashboardView.as_view(), name="dashboard"),
    path("admin_list/", AdminUserListView.as_view(), name="admin_list"),
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("admin_create/", AdminUserCreateView.as_view(), name="admin_create"),
    path("delete/<int:user_id>/", UserDeleteView.as_view(), name="delete"),
]
