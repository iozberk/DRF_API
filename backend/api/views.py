# from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view





@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    """
    DRF ApiView
    """
    if request.method != 'POST':
        return Response({'detail': 'GET not allowed'}, status=400)
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','content','price'])
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





