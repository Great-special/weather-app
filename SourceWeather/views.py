from django.shortcuts import render
import urllib.request as api_request
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        # api_url = api_request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=ad6d91c541e7f84004e3201f55d89a05').read()
        api_url = api_request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=2324b76275971d0180fc2c0adf80dccf').read()
        api_response = json.loads(api_url)
        print(api_response)

        data = {
            "country": api_response['sys']['country'],
            "longitude": api_response['coord']['lon'],
            "latitude": api_response['coord']['lat'],
            "weather_description": api_response['weather'][0]['description'],
            "weather_temperature": api_response['main']['temp'],
            "weather_pressure": api_response['main']['pressure'],
            "weather_humidity":api_response['main']['humidity'],
            "weather_icon": api_response['weather'][0]['icon'],
        }
        
    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity":None,
            "weather_icon": None,
        }
    print(data['weather_icon'])
    context = {
        "city": city,
        "data" :data
    }
    return render(request, 'index.html', context)
    
    
