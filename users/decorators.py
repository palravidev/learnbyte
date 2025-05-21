from django.shortcuts import render
from functools import wraps

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.role == required_role:
                return view_func(request, *args, **kwargs)
            return render(request, '403.html', status=403)
        return wrapper
    return decorator
