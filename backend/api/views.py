from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    print(request.body)
    data = {

    }
    return JsonResponse({"message": "this is sumit"})
