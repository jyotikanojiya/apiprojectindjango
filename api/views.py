from django.shortcuts import render 
import io
from rest_framework.parsers import JSONParser
from .models import WeatherData
from .serializers import WeatherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def WeatherView(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                wea = WeatherData.objects.get(id=id)
                serializer = WeatherSerializer(wea)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except WeatherData.DoesNotExist:
                return JsonResponse({'error': 'Weather data not found'}, status=404)
    
        # If 'id' is not provided, return all WeatherData
        wea = WeatherData.objects.all()
        serializer = WeatherSerializer(wea, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    #post method
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parser = JSONParser()
        pythondata = parser.parse(stream)
        serializer = WeatherSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data saved'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    
    #put
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parser = JSONParser()
        pythondata = parser.parse(stream)
        id = pythondata.get('id')
        wea = WeatherData.objects.get(id =id)  #patialupdate
        serializer = WeatherSerializer(wea, data = pythondata , partial= True) #humidity is not change #all data not required
        # serializer = WeatherSerializer(wea, data = pythondata ) # all data required
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    
    #delete 
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parser = JSONParser()
        pythondata = parser.parse(stream)
        id = pythondata.get('id')
        wea = WeatherData.objects.get(id =id)
        wea.delete()
        res = {'msg': 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type="application/json")

