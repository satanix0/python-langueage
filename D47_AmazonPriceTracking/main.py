import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/WarsTM-Instant-Pressure-Cooker-VaderTM/dp/B08DZ3W578/ref=pd_rhf_d_dp_s_pd_ldate_sccl_2_3/133-9984859-3967409?pd_rd_w=aVhsY&content-id=amzn1.sym.c652f708-20a7-4738-ae35-3e3b80fab45e&pf_rd_p=c652f708-20a7-4738-ae35-3e3b80fab45e&pf_rd_r=A827GBXR0WJBKA1GGT0E&pd_rd_wg=hxdcu&pd_rd_r=476e1b2c-653a-406d-a684-23f0a17f3a0f&pd_rd_i=B08DZ3W578&psc=1'
headers = {'Accept-Language': 'en-US,en;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', }
respnse = requests.get(
    url=URL,
    headers=headers)

soup = BeautifulSoup(respnse.text, 'lxml')

price = soup.find(name='span', class_='a-offscreen')

price_d = float(price.getText().strip('$'))

# Sending an email when price goes down
import smtplib

my_mail = 'pythoncode172@gmail.com'
password = 'kmyqhhcmqsysczwa'
if price_d < 100:
    sent = f"Hey Price for {soup.title.text} went down.\nNow available for ${price_d} only.\nClick here to buy now : {URL}".encode("utf-8")
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs='piyushkr172@gmail.com', msg=f'Subject:Price went down\n\n{sent}')
    connection.close()
    print("Email Sent Successfully")

print("Program Closed Successfully")
