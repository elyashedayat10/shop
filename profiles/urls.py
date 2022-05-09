from django.urls import path
from .views import ProfileUpdateView

app_name = 'profile'
urlpatterns = [
    path('update/<int:profiel_id>/', ProfileUpdateView.as_view(), name='update'),
]
