from .models import WeatherData
from rest_framework import routers, serializers, viewsets

# class WeatherSerializer(serializers.Serializer):
#     city = serializers.CharField(max_length=255)
#     temperature = serializers.FloatField()
#     humidity = serializers.FloatField()
#     weather_description = serializers.CharField(max_length=255)
#     timestamp = serializers.DateTimeField(auto_now_add=True)

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'  


def create(self,validated_data):
    return WeatherData.objects.create(**validated_data)


def update(self,instance , validated_data):
    print(instance.city)
    instance.city = validated_data.get('city', instance.name)
    print(instance.city)
    instance.temperature = validated_data.get('temperature', instance.temperature)  
    print(instance.humidity) 
    instance.humidity = validated_data.get('humidity', instance.humidity)
    print(instance.humidity)  #humidity is not change

    instance.weather_description = validated_data.get('city', instance.weather_description)
    instance.save()
    return instance
 

