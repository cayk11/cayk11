from urlib.request import urlopen
import json

api_key = "xxxxxxx"

def get_weather(city):
    sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" +
                           city + "&appid=" + api_key)
    result = sock.read()
    sock.close()
    weather = json.loads(results)
    return weather["main]["temp"] -273.15
    
if __name__ == "__main__":
    degrees = get_weather("OLSO")
    print("Weather in Olso is %.2f degrees Celsius" % degrees)
