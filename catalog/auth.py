from django.conf import settings
from django.http import JsonResponse

def require_api_key(view_func):
    def wrapper(request, *args, **kwargs):
        api_key = args[0].headers.get('X-API-Key')
        print(f"Received API Key :{type(args),kwargs }")
        print("f", request.headers)
        if api_key not in settings.VALID_API_KEYS:
            return JsonResponse({
                "error": "INVALID_API_KEY",
                "message": "Missing or invalid API key"
            
            }, status=401)
        return view_func(request, *args, **kwargs)
    
    return wrapper
