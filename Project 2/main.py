# Weather App using OOP by Sami

import requests # Imports requests library 

# Class function with constructor and parameters.  
class WeatherApp:
    def __init__(self, key):
        self.key = key

    # Retrieves data based on location and converts the json file to a python dictionary. 
    def getweather(self, location): 
        url = f"http://api.weatherapi.com/v1/current.json?key={self.key}&q={location}" # Url with key and location
        response = requests.get(url) # Connection to the url server and receiving back requested data. 
        data = response.json()

        if 'error' in data:
            return None
        
        weatherdata = {
            'location': data['location']['name'],
            'country': data['location']['country'],             
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind': data['current']['wind_kph']
        }

        return weatherdata

# Main function that asks the user for location. 
def main():
    key = '7cffeb3c2e414cb69da31228231206' # My API key
    app = WeatherApp(key)

    while True:
        print("\nWeather App")
        print("1. Find the weather in an area.")
        print("2. Exit.")
        choice = input("Enter a selection (1-2): ")

        if choice == "1":
            location = input("Enter a location: ")
            weatherdata = app.getweather(location)

            if weatherdata is not None:
                print("\nWeather Information:")
                print(f"Location: {weatherdata['location']}, {weatherdata['country']}")
                print(f"Temperature: {weatherdata['temperature']}°C")
                print(f"Condition: {weatherdata['condition']}")
                print(f"Humidity: {weatherdata['humidity']}%")
                print(f"Wind: {weatherdata['wind']} kph")
            else:
                print("\nError: Invalid Location")
        elif choice == '2':
            break
        else:
            print("\nPlease enter a selection that is either 1 or 2.")

# Start
main()


# Example of how to access the weatherdata dictionary.
 
# Import requests

# key = 'api_key' - This key is different for everyone and so it depends on the website. 
# location = 'Any Location'
# url = "The base URL which should be given by the website but you have to add your key and location variables to the url."
# response = requests.get(url)
# data = response.json()

# print(data) - This prints the dictionary of that location, and we are easily able to access all data inside the dictionary.
# If the name of the location is an invalid location, it will print an 'error' dictionary. 