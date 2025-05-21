from django.urls import path
from .views import account_settings_view

urlpatterns = [
    path('dashboard/settings/', account_settings_view, name='account_settings'),
]