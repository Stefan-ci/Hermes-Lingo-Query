from django.conf import settings

def site(request):
    context = {
        "site_name": settings.SITE_NAME,
    }
    return context
