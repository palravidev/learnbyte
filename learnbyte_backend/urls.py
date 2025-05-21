from django.contrib import admin
from django.urls import path, include
from . import views  # For home, student/teacher dashboards
from users.views import role_based_redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # Allauth handles signup, login, logout, password reset, email confirmation
    path('accounts/', include('allauth.urls')),

    # Public & role-based views
    path('', views.home_view, name='home'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('accounts/profile/', role_based_redirect, name='account_profile'),
    path('accounts/redirect/', role_based_redirect, name='account_profile'),
]
