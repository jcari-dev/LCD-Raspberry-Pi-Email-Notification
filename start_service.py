import requests
import json
import re
from geodecode import decode_postal_code as decode
from geodecode import supported_countries


# response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")

# print(response.json())

while 1:
    
    get_weather = input('Do you wish to add local weather to your PI LCD? (y/n)')

    if get_weather.lower() not in ('y', 'n'):
        print("Incorrect input, please enter 'Y' for yes, or 'N' for no. If you wish to terminate the program press CTRL+C")
    else:
        break

if get_weather == 'n':
    print('Excellent, weather functionality skipped.')
else:
    cont = False
    while cont == False:
        
        country = input("Enter 2 letter country code (ISO Alpha-2), e.g. 'FR' for France.")
        
        if country.upper() not in supported_countries.country_codes:
            print("We're sorry, your country is currently not supported. Skipping weather functionality.")
            exit()
            
        else:
            valid_country = True
            
        postal_code = input("Enter the 5 digit postal code e.g. '90001' ")
        
        if re.match(r"^[0-9]{5}(?:-[0-9]{4})?$", postal_code) != None:
            valid_postal_code = True
        
        if valid_postal_code == True and valid_country == True:
            lat_lon = decode.get_lat_lon(country,postal_code)
            weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat_lon['lat']}&longitude={lat_lon['lon']}&current_weather=true&timeformat=unixtime"
            weather_data_request = requests.get(weather_api_url)
            weather_data = weather_data_request.json()
            cont = True

weather_file = open("user_weather_data.txt", "a")

weather_file.write(weather_api_url)

weather_file.close()

print(f"°{weather_data['current_weather']['temperature']}C / °{round((weather_data['current_weather']['temperature'] - 32) * 5/9, 1)}F")