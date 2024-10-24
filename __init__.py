from flask import Flask, render_template,request
from weather_service import wAPI
import requests

app = Flask(__name__)




@app.route("/", methods=("POST","GET"))
def weather():

    details = {
        "locations":[],
        "lon_code" : [],
        "lat_code" : []
    }
  
    output = []
    
    if request.method == "POST":
        form_type = request.form.get("form_type")
        if form_type == "city_name":
            cityname = request.form["city"]
            city_codes = wAPI.get_city_code(cityname)

            if city_codes == "Location not found":
                return render_template("weather.html", message="Location not found")
            else:
                for items in city_codes:
                    lat = items["lat"]
                    details["lat_code"].append(lat)
                    lon = items["lon"]
                    details["lon_code"].append(lon)
                    location = items["name"],items.get("state", "N/A")
                    details["locations"].append(location)
                
        if form_type == "city_details":
            lat = request.form["lat"]
            lon = request.form["lon"]
            weatheroutput = wAPI.weather_details(lat,lon)
            output.append(weatheroutput)
        
    elif request.method == "GET":
        return render_template("weather.html")



    return render_template("weather.html", details = details,output = output)

# get_city_code()

if __name__ == ("__main__"):
    app.run(debug=True)