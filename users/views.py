# ✅ File: users/views.py
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from .forms import AccountSettingsForm

@role_required('student')
@login_required
def student_dashboard(request):
    return render(request, 'dashboard/student.html')

@role_required('instructor')
@login_required
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher.html')

@never_cache
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

@login_required
def role_based_redirect(request):
    next_url = request.GET.get('next') or request.POST.get('next')
    if next_url:
        return redirect(next_url)
    user = request.user
    if user.role == 'student':
        return redirect('student_dashboard')
    elif user.role == 'instructor':
        return redirect('teacher_dashboard')
    else:
        return redirect('home')

# 🔽 New: Account Settings View
@login_required
def account_settings_view(request):
    user = request.user
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('account_settings')
    else:
        form = AccountSettingsForm(instance=user)
    return render(request, 'dashboard/account_settings.html', {'form': form})
