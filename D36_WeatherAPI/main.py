import requests as r
from twilio.rest import Client
account_sid = 'ACf82b836161b2de704a15f8cf673e5b3f'
auth_token = '01709871b99157a58063e886bd76abd9'
parameters = {
    "lat": 37.566536,
    "lon": 126.977966,
    "exclude": "current,daily,minutely",
    "appid": "49ff9f8d305b69eb77dde31b1242bd4e",
}

MY_MAIL = 'pythoncode172@gmail.com'
PASS = 'kmyqhhcmqsysczwa'

response = r.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
twlv_hr = weather_data['hourly'][0:12]
will_rain = False
for i in range(0, len(twlv_hr)):
    weath_id = twlv_hr[i]['weather'][0]['id']
    if weath_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='You should take an Ubmbrella ☔',
        from_='+18126386198',
        to='+916209675038'
    )
    print(message.sid)
