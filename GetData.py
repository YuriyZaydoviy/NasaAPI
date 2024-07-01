#importing libs
import requests
from datetime import datetime
#importing settings file
from Settings import *
#main munction
def get_array():
    
    #get json file 
    json = get_json(nasa_api,nasa_url)
    #get date for today's asteroids
    date = get_date_today()
    #from json to 2d array
    asteroids = get_data(json,date)
    return asteroids

#function to get date to use in get_json() and main() function
def get_date_today():
    #format of data is important,only this format
    today = datetime.today().strftime("%Y-%m-%d")
    return today
#getting json file
def get_json(nasa_key,nasa_url):
    today_date = get_date_today()
    nasa_url = nasa_url + today_date +"&end_date="+ today_date + "&api_key="+nasa_key
    #get from nasa site
    nasa_response = requests.get(nasa_url)
    json = nasa_response.json()
    return json
#from json to array
def get_data(json_nasa,today_date):
    #accesing the json data as usual
    #get the count
    asteroids_count = json_nasa["element_count"]
    asteroids_array_json = json_nasa["near_earth_objects"][today_date]

    #array that will be returned
    asteroids_array = []
    asteroids_array.append(asteroids_count)
    #information of every asteroid
    for aster in asteroids_array_json:
        #name,id
        name = aster["name"]
        id = aster["id"]
        #max and min diameter - in meters
        diam_min = aster["estimated_diameter"]["meters"]["estimated_diameter_min"]
        diam_max = aster["estimated_diameter"]["meters"]["estimated_diameter_max"]
        #is_hazard - true/false
        is_hazardous = aster["is_potentially_hazardous_asteroid"]
        #date in string format,YYYY-MM-DD
        close_approach_data = aster['close_approach_data']
        for approach in close_approach_data:
            #approach date YYYY-MM-DD string
            approach_date = approach['close_approach_date']
            #velocity,kilometers per second
            velocity_kmps = approach['relative_velocity']['kilometers_per_second']
            #distance
            min_distance_km = approach['miss_distance']['kilometers']
        #appending data
        asteroids_array.append([name,id,float(diam_min),float(diam_max),bool(is_hazardous),approach_date,float(velocity_kmps),float(min_distance_km)])
        #print("\n\n\nASTEROID","\nNAME:",name,"\nID:",id,"\nDIAMETER(meters):",(diam_max+diam_min)/2,"\nIS HAZARDOUS:",is_hazardous,"\nAPPROACH DATE:",approach_date,"\nVELOCITY(km per second):",velocity_kmps,"\nMIN DISTANCE(km):",min_distance_km)
    return asteroids_array


