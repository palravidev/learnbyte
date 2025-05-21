from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required


@role_required('student')
@login_required
def student_dashboard(request):
    return render(request, 'dashboard/student.html')

# Instructor Dashboard (Restricted)
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

    # Fallback: role-based dashboard
    user = request.user
    if user.role == 'student':
        return redirect('student_dashboard')
    elif user.role == 'instructor':
        return redirect('teacher_dashboard')
    else:
        return redirect('home')