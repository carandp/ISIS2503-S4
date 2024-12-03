from django.shortcuts import redirect
from django.contrib.auth import logout

from monitoring.auth0backend import getRole

def admin_required(view_func):
    """
    Decorator for views that checks that the user is logged in and is an admin,
    logging out the user if necessary.
    """
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated or not getRole(request) == "admin":
            logout(request)
            return redirect('/instituciones/create/')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func