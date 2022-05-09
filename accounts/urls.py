from django.urls import path
from .views import (
    UserAuthView,
    UserVerifyView,
    UserLogoutView,
)

app_name = 'accounts'
urlpatterns = [
    path('auth/', UserAuthView.as_view(), name='auth'),
    path('verify/', UserAuthView.as_view(), name='verify'),
    path('logout/', UserAuthView.as_view(), name='logout'),
]
