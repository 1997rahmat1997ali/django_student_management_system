import imp
from multiprocessing import context
from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    city = request.GET.get('city', "Lucknow")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=22093d6a3f26e74036ac481b4eed0935'
    data = requests.get(url).json()
    #print(data)

    payload = {
    'city' : data['name'], 
    'weather': data['weather'][0]['main'],
    'icon' : data['weather'][0]['icon'], 
    'kelvin_temprature' : data['main']['temp'],
    'celcius_temprature' : int(data['main']['temp']-273), 
    'pressure' : data['main']['pressure'], 
    'humidity' : data['main']['humidity'],
    'description' : data['weather'][0]['description']
    }

    context = {'data' : payload}
    print(data)

    return render(request,'home.html',context)