from geopy.geocoders import Nominatim

def coordinates_finder():
    geolocator = Nominatim(user_agent="my_user_agent")
    city = input("Enter City: ")
    while not city:
        print("Please enter a city")
        city = input("Enter City: ")
    country = input("Enter Country: ")
    while not country:
        print("Please enter a country: ")
        country = input("Enter Country: ")
    if ValueError:
        print("Invalid Coordinates")
        city = input("Enter City: ")
        while not city:
            print("Please enter a city")
            city = input("Enter City: ")
        country = input("Enter Country: ")
        while not country:
            print("Please enter a country: ")
            country = input("Enter Country: ")
    loc = geolocator.geocode(city+','+ country)
    print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
coordinates_finder()