import requests
import time 
import time
global pstcode

def weathercheck_1(postcode_raw):
    global pstcode
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()

    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")

    print("Let me just check the weather there today...\n")


    for i in range(3):
        time.sleep(1)
        print("...")

def weathercheck_2(postcode_raw):
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    area = postcode_resp['result']['admin_ward']
    

    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")