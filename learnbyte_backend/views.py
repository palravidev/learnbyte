from django.shortcuts import render
from django.views.decorators.cache import never_cache
from users.decorators import role_required

@never_cache
def home_view(request):
    return render(request, 'home.html')

@never_cache
@role_required('instructor')
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher.html')

@never_cache
@role_required('student')
def student_dashboard(request):
    return render(request, 'dashboard/student.html')
