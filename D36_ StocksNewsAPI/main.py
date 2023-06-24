import requests as r
from datetime import date, timedelta, datetime
from twilio.rest import Client
# twilio API Creds
account_sid = 'ACf82b836161b2de704a15f8cf673e5b3f'
auth_token = '01709871b99157a58063e886bd76abd9'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_MAIL = 'pythoncode172@gmail.com'
PASS = 'kmyqhhcmqsysczwa'

# Stocks Info API
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
STOCK_APIKEY = "F8ZTMNWPF65DFTAD"
stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_APIKEY
}

response = r.get(url=STOCK_ENDPOINT, params=stock_param)
data = response.json()
# print(data)

today = date.today()
yesterday = today - timedelta(days=1)    # getting date for yesterday
# getting date for a day before yesterday
day_bfr_ystr = today - timedelta(days=2)
# converting date for yesterday to string format
yestrstr = yesterday.strftime('%Y-%m-%d')
# converting date for day before yesterday to string format
day_bfr_str = day_bfr_ystr.strftime('%Y-%m-%d')

'''
Instead we can also use 'list comphrehension' to get the values of closing prices
all we need to do is

prev_days_list = [value for (key, value) in data.items()]
yesterday_data = prev_days_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_bfr_ystrday_data = prev_days_list[1]
day_bfr_clsng_price = day_bfr_ystrday_data["4. close"]
'''

# getting yesterday's closing value
yester_clsng = float(data['Time Series (Daily)'][yestrstr]['4. close'])
day_yestr_clsng = float(data['Time Series (Daily)'][day_bfr_str]['4. close'])

# Absolute value of closing price difference
clsing_diff = yester_clsng - day_yestr_clsng
up_down_emoji = None
if clsing_diff > 0:
    up_down_emoji = '📈'
else:
    up_down_emoji = '📉'

# percentage of difference
diff_percent = round(clsing_diff/yester_clsng)*100


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "ab5bc489467843f6bae4a185bac90774"

if abs(diff_percent) > 0.5:
    news_params = {
        "q": COMPANY_NAME+" shares",
        "apiKey": NEWS_APIKEY
    }

    news_response = r.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    news_list = news_data['articles'][0:3]


# Using twilio.com/docs/sms/quickstart/python
    # List of texts to be sent
    final_text = [
        f"{STOCK} : {up_down_emoji}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_list]
# Send a separate message with each article's title and description to your phone number.
    client = Client(account_sid, auth_token)
    for article in final_text:
        message = client.messages.create(
            body=article,
            from_='+18126386198',
            to='+916209675038'
        )
