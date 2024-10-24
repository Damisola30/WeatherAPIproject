import httpx
import requests
import os
from dotenv import find_dotenv,load_dotenv
from datetime import datetime, timedelta

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
api_key = os.getenv("API_KEY")

def get_local_time(timestamp, timezone_offset):
    # Step 1: Convert Unix timestamp to UTC datetime
    utc_time = datetime.utcfromtimestamp(timestamp)

    # Step 2: Adjust for timezone offset
    local_time = utc_time + timedelta(seconds=timezone_offset)

    # Step 3: Format the time in 12-hour standard format with AM/PM
    return local_time.strftime('%I:%M:%p')


class wAPI():
    api_key = "api_key"
    def get_city_code(city_name):
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}'
        codes = requests.get(url).json()
        if not codes:  
            return "Location not found"
        return codes
    
    def weather_details(lat_code, lon_code):
        weatherurl = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_code}&lon={lon_code}&appid={api_key}'
        result = requests.get(weatherurl).json()
        timezone = result["timezone"]
        timestamp = result["dt"]
        time = get_local_time(timestamp, timezone)            
        icon_code =  result["weather"][0]["icon"]
        deg = round(float(result["main"]["temp"]) - 273.15,2)
        description = result["weather"][0]["description"]
        wind_speed = result["wind"]["speed"]
        humidity = result["main"]["humidity"]
        name = result["name"]
        output = [ timezone, timestamp, time, icon_code, deg, description, wind_speed,  humidity,name]
        return output
    









        
    



# What's remaining 
# implementing the search function: when the user inputs a place and clicks search,| i'll try and implement the AJAKS on this to prevent it from reloading instead it will send the name to the url and get a response {code} in real time |
# it will send the name to the get_city_code function ,then it will return a search box {codes} containing the various place's state and lat and lon code fo each of them (displaying only the {location})
# when the user  selects an option ,that option will then trigger and send the lon and lat of the location to the weather details function, the response(details) will then update the useful information in the weather box on the page