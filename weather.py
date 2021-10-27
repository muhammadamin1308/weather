import eel
import pyowm

owm = pyowm.OWM("513c4d20ab89b36b3a99a0d5eadaafaa")

@eel.expose
def get_weather(place):
    city = "New York, USA"


    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    print("In the region " + city +  str(temp) + " celsies now")



eel.init("web")

eel.start("weather.html", size=(700, 700))    






# from pyowm import OWM

# owm = OWM('513c4d20ab89b36b3a99a0d5eadaafaa')
# place = input("Place:")

# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(place)
# w = observation.weather
# t = w.temperature("celsius")
# t1 = t['temp']
# print(t1)






# import eel 

# @eel.expose
# def pprint():
#     print("Hello World!")

# eel.init("web")
# eel.start("new.html")