import time
import requests
from datetime import datetime

MY_LAT = 47.346279 # Your latitude
MY_LONG = 22.340090 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])




parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def search_iss():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()


    if iss_longitude>MY_LONG-5 and iss_longitude<MY_LONG+5 and iss_latitude>MY_LAT-5 and iss_latitude<MY_LAT+5:
        my_time = str(time_now)
        my_time = my_time.split(' ')[1].split(':')
        my_hour = int(my_time[0])
        if (my_hour < sunrise or my_hour > sunset):
            print('It is Nighttime')
            print('The iss is above you right now!')
            return 1


while True:
    if(search_iss()==1):
        break
    else:
        print("The conditions are wrong")
        print("Waiting for 60 seconds")
    time.sleep(60)






