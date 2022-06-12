from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# using models drf way'

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    if request.method == 'GET':
        instance = Product.objects.all().order_by("?").first()
        data = ProductSerializer(instance).data
        return Response(data)
    else:
        data = request.data
        print(data)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(data)
        return Response("data not valid")



# 'using models smart way'
def api_home_old_2(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)


# using models but hard way'
def api_home_old_1(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
    return JsonResponse(data)


# 'old traditional way'
def api_home_old(request, *args, **kwargs):
    print(request.body)
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    print(data)
    data['content_type'] = request.content_type
    data['params'] = request.GET
    return JsonResponse(data)
