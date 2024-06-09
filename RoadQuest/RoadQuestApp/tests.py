from django.test import TestCase
from amadeus import ResponseError, Client

amadeus = Client(
        client_id='5vFjQOyy1Dmb5frlsK8PcGQOLgjMuLyZ',
        client_secret='u5D2xe5MoY1Vyi0j'
)

def get_hotels(longitude, latitude):
    try:
        response = amadeus.reference_data.locations.hotels.by_geocode.get(
            longitude = longitude, 
            latitude = latitude
        )
        return response.data
    except ResponseError as error:
        raise error
    

def main():
    longitude = -122.97286378718171
    latitude = 49.27818323982278
    
    try:
        hotels_data = get_hotels(latitude, longitude)

        print("Retrieved Hotel Data:")
        print(hotels_data)
    except ResponseError as error:
        print("An error occurred while retrieving hotel data:")
        print(error)

main()


