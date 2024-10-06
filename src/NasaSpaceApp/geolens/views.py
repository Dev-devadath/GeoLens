from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import requests

@csrf_exempt
def get_soil_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lat = data.get('lat')
        lon = data.get('lon')

        # Replace this URL with the actual OpenEPI Soil API endpoint
        api_url = "https://api-test.openepi.io/soil/type"
        params = {
            'lat': lat,
            'lon': lon,
            'top_k': 3
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            soil_data = response.json()
            # Extract most probable soil type from properties
            most_probable_soil_type = soil_data['properties']['most_probable_soil_type']

            # You can also access probabilities if needed
            probabilities = soil_data['properties']['probabilities']

            # Format probabilities into a more readable structure if required
            formatted_probabilities = [
                {
                    'soil_type': prob['soil_type'],
                    'probability': prob['probability']
                }
                for prob in probabilities
            ]

            return JsonResponse({
                'most_probable_soil_type': most_probable_soil_type,
                'probabilities': formatted_probabilities  # Include if you need it on the frontend
            })
        else:
            return JsonResponse({'error': 'Error fetching data from API'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def index(request):
    return render(request, "index.html")