# from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer




@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF ApiView
    """
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id','title','content','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)


















    # print(request.GET)
    # print(request.POST)
    # body = request.body # byte string of Json data
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass    
    # print(data)
    # # data['headers'] = request.headers
    # print(request.headers)
    # data['params'] = dict(request.GET) 
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type





