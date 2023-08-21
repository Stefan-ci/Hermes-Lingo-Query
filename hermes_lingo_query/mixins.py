from accounts.models import User
from django.http import JsonResponse
from django.contrib.auth.mixins import AccessMixin


class ApiKeyRequiredMixin(AccessMixin):
    """ Verify that a valid API Key has been provided in headers
        
        1. Check if user is authenticated, then get current logged in user API key
        
        2. If an API key has been provided in the headers:
            - Check if `api-key´ is valid and not suspended.
        
        3. If an API key has been provided in request parameters:
            - Check if `api-key´ is valid and not suspended.
            
        Else:
            - Not provided API key
    """
    
    def dispatch(self, request, *args, **kwargs):
        # Login based
        if request.user.is_authenticated:
            if not request.user.is_suspended and request.user.api_key is not None:
                return super().dispatch(request, *args, **kwargs)
            return JsonResponse({"error": "Account suspended!"}, status=403, safe=False)
        
        # Request parameters based
        try:
            api_key = request.GET.get("x-api-key") or None
            if api_key is not None:
                try:
                    user = User.objects.get(api_key=api_key, is_active=True)
                    if user.is_suspended or not user.is_active:
                        return JsonResponse({"error": "Account suspended!"}, status=403, safe=False)
                    return super().dispatch(request, *args, **kwargs)
                except User.DoesNotExist:
                    return JsonResponse({"error": "API key is not valid!"}, status=404, safe=False)
                except:
                    return self.handle_no_permission()
            else:
                pass
        except:
            pass
        
        # Headers based
        try:
            api_key = request.headers.get("x-api-key") or None
            if api_key is not None:
                try:
                    user = User.objects.get(api_key=api_key, is_active=True)
                    if user.is_suspended or not user.is_active:
                        return JsonResponse({"error": "Account suspended!"}, status=403, safe=False)
                    return super().dispatch(request, *args, **kwargs)
                except User.DoesNotExist:
                    return JsonResponse({"error": "API key is not valid!"}, status=404, safe=False)
                except:
                    return self.handle_no_permission()
            else:
                return JsonResponse({"error": "API key has not been provided!"}, status=404, safe=False)
        except:
            return JsonResponse({"error": "API key has not been provided!"}, status=404, safe=False)
