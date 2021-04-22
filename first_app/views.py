from django.shortcuts import render, redirect
import requests, json
from .models import Weather

def index(request):
    return render(request, 'index.html')

def check(request):
    city = request.POST['city']
    state = request.POST['state']
    zip_code = request.POST['zip']


    result = requests.get(f'http://api.weatherapi.com/v1/current.json?key=4f4b67d5b5a647d5a6c24042212204&q={city},{state},{zip_code}&aqi=no').json()

    location_city = result['location']['name']

    location_state = result['location']['region']

    weather_f = result['current']['temp_f']

    weather_c = result['current']['temp_c']

    weather_text = result['current']['condition']['text']

    weather_icon = result['current']['condition']['icon']

    weather_humidity = result['current']['humidity']

    weather = Weather.objects.create(
        city = location_city,
        state = location_state,
        weather_f = weather_f, 
        weather_c = weather_c,
        weather_t = weather_text,
        weather_i = weather_icon,
        weather_h = weather_humidity,
        )

    context = {
        'weather': weather,
    }

    return render(request, 'partial.html', context)



