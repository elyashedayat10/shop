from django.urls import path

from .views import (UserAuthView, UserDashboardView, UserLogoutView,
                    UserVerifyView)

app_name = 'account'
urlpatterns = [
    path('auth/', UserAuthView.as_view(), name='auth'),
    path('verify/', UserVerifyView.as_view(), name='verify'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('dashboard/', UserDashboardView.as_view(), name='dashboard'),
]
