from django.contrib import messages
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if "next" in request.POST or "next" in request.GET:
                return redirect(request.POST.get("next") or request.GET.get("next"))
            messages.warning(request, "You're already logged in!")
            return redirect(request.META.get("HTTP_REFERER") or "core:home")
        return view_func(request, *args, **kwargs)
    return wrapper_func
