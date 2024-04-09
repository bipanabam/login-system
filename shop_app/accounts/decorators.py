from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    """ If user is already authenticated, they can't view this page .i.e. login or register """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_type=[]):
    """Restricting views based on user_type"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.user_type:
                type = request.user.user_type
            if type in allowed_type:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You aren't authorized to view this page.")
        return wrapper_func
    return decorator