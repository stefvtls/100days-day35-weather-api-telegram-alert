import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY35_WEATHER = os.getenv("API_KEY35_WEATHER")
LAT35 = os.getenv("LAT35")
LON35 = os.getenv("LON35")
BOT_TOKEN35 = os.getenv("BOT_TOKEN35")
BOT_CHAT_35_ID = os.getenv("BOT_CHAT_35_ID")

parameters = {"lat": LAT35, "lon": LON35, "appid": API_KEY35_WEATHER, "exclude": "current,minutely,daily"}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()
data = response.json()
weather_list = []
will_rain = False
for times in range(12):
    hour_data = data["hourly"][times]["weather"][0]["id"]
    if hour_data < 700:
        will_rain = True


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN35 + '/sendMessage?chat_id=' + BOT_CHAT_35_ID + '&parse_mode=Markdown&text=' + bot_message
    response2 = requests.get(send_text)
    return response2.json()

if will_rain:
    test = telegram_bot_sendtext("Bring an umbrella")
