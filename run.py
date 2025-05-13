from geopy.geocoders import Nominatim
from replit import clear

geolocator = Nominatim(user_agent="my_user_agent")

def city_and_country_input():
    city = input("Enter City: ")
    while not city:
        print("Please enter a city")
        city = input("Enter City: ")
    country = input("Enter Country: ")
    while not country:
        print("Please enter a country: ")
        country = input("Enter Country: ")    
    coordinates_finder(city, country)

def coordinates_finder(city, country):
        loc = geolocator.geocode(city+','+ country)
        if loc is None:
            print("Unable to find your location try again")
            city_and_country_input()
        else:
            print("\nlatitude is : " ,loc.latitude, "|" " longtitude is:" ,loc.longitude)
            continue_or_not()

def continue_or_not():
    clear_console = input(
            "\nWould you like to clear the console? (yes/no): "
        ).lower()
    if clear_console in ["yes", "y"]:
        clear()
        city_and_country_input()
    if clear_console in ["no", "n"]:
        print("\n")
        city_and_country_input()
    while clear_console not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        clear_console = input(
            "Would you like to clear the console? (yes/no): "
        ).lower()


city_and_country_input()