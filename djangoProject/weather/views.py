from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):56b7cde56495f5f'
    url = 'TAKE YOUR API KEY FROM OPENWEATHERMAP'

    # Retrieve all cities from the database
    cities = City.objects.all()

    # Handle form submission
    if request.method == 'POST':  # Only true if a form is submitted
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()  # Save only if the form is valid

    # Prepare weather data for all cities
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()  # Use the city's name attribute
        if city_weather.get('main'):  # Ensure the API returned valid data
            weather = {
                'city': city.name,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)

    # Prepare the form for the template
    form = CityForm()

    # Pass data to the template
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)






