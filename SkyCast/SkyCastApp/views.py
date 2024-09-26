from django.shortcuts import render
import requests
from django.conf import settings

def get_coordinates(city):
    api_key = settings.OPENWEATHER_API_KEY  
    geocode_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(geocode_url)
    data = response.json()
    if data.get('cod') == 200:
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        return lat, lon
    return None, None

def get_forecast_data(lat, lon):
    api_key = settings.OPENWEATHER_API_KEY  
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    response = requests.get(forecast_url)
    data = response.json()
    if data.get('cod') == '200':
        return data
    return None

def index(request):
    weather_data = None
    forecast_data = None
    
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            lat, lon = get_coordinates(city)
            if lat and lon:
                
                weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
                try:
                    weather_response = requests.get(weather_url)
                    weather_data = weather_response.json()
                    
                    if weather_data.get('cod') == 200:
                        weather_data = {
                            'city': weather_data['name'],
                            'country_code': weather_data['sys']['country'],
                            'coordinate': f"{weather_data['coord']['lat']}, {weather_data['coord']['lon']}",
                            'temp': weather_data['main']['temp'],
                            'pressure': weather_data['main']['pressure'],
                            'humidity': weather_data['main']['humidity'],
                            'description': weather_data['weather'][0]['description'],
                            'icon': weather_data['weather'][0]['icon']
                        }
                    else:
                        weather_data = {'error': 'City not found'}
                    
                except Exception as e:
                    weather_data = {'error': str(e)}

                # Fetch 5-day forecast
                forecast_data = get_forecast_data(lat, lon)

    return render(request, 'main/index.html', {'weather_data': weather_data, 'forecast_data': forecast_data})
