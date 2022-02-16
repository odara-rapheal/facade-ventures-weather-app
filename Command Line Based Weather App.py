# importing necessary libraries
import requests
from prettyprinter import pprint
from time import sleep

# creating cities of operation and their respective number
cities_list = {1:"Lusaka", 2:"Johannesburg", 3:"Lagos State", 4:"Accra", 5:"Nairobi"}

# delayng the program runtime and asking the user for their full name
sleep(2)
print("Welcome to Facade Ventures Weather App")
sleep(2)
name = input("What is your full name? (Format: First Name then Last Name): ")
sleep(1)

# welcoming the user and displaying cities of operation
print(f"Welcome, {name}!")
sleep(2)
print("Here is a list of available cities (and countries)")
for num, city in cities_list.items():
    print(num, city)
    
# accepting input on city selected
city_no = int(input("Enter a number from the options above to select a city you want info on: "))
sleep(1)

# assigning city selected to a variable
city_selected = cities_list[city_no]

# sending an http request
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_selected}&appid=050d64dfdbd609c8bcb00ef5e6f6b2db&units=metric")

# storing the http response in a json file/format
data = response.json()

# assigning required weather info to a variable
country = data["sys"]["country"]
degree_sign = u'\N{DEGREE SIGN}'
weather_data = data["weather"][0]["description"]
cloud = data["clouds"]["all"]
min_temp = data["main"]["temp_min"]
max_temp = data["main"]["temp_max"]
wind_speed = data["wind"]["speed"]
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]

# displaying waeather information on screen
sleep(2)
print(f"[INFO] Getting info on {city_selected} ({country})...")
sleep(2)
print(f"[INFO] You have asked for weather information on {city_selected}.")
sleep(2)
print(f"[INFO] Please be patient while we attend to your request...")
sleep(3)
print(f">>> Today's forcast for {city_selected} is {weather_data}")
sleep(1)
print(f">>> It is also {cloud}% cloudy today in {city_selected}.")
sleep(1)
print(f">>> With a minimum temperature of {min_temp}{degree_sign}C.")
sleep(1)
print(f">>> And a maximum temperature of {max_temp}{degree_sign}C.")
sleep(1)
print(f">>> The wind blows at {wind_speed}m/s.")
sleep(1)
print(f">>> The pressure at {city_selected} is {pressure}hpa.")
sleep(1)
print(f">>> And it is {humidity}% humid.")
sleep(3)
print(f"[INFO] Getting location details for {city_selected}...")
sleep(2)
print(f">>> {city_selected} is located at latitude {latitude} and longitude {longitude}.")
sleep(2)
print(f"[INFO] Request completed!")

# end of program
sleep(1)
input("press ENTER key to exit")
