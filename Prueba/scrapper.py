import requests as rq
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.es/Nikon-D5600-18-140-3-5-5-6-Nikkor/dp/B01MXSJOAM/ref=pd_sbs_421_4/258-3304029-4666252?_encoding=UTF8&pd_rd_i=B01MXSJOAM&pd_rd_r=d8583cc7-c49c-4555-8458-922376152c88&pd_rd_w=OI7h8&pd_rd_wg=L7Ev0&pf_rd_p=f9384d3f-fa3d-4e25-8bc3-b0c7853cd8a6&pf_rd_r=NAPVMJNMWQ3GZRZT57FR&psc=1&refRID=NAPVMJNMWQ3GZRZT57FR'

header = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.100 Safari/537.36"}


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("xxxx@gmail.com", "passwrd.")
    subject  = 'prueba precio'
    body = "Esta es una prueba para revisar el link : https://www.amazon.es/Nikon-D5600-18-140-3-5-5-6-Nikkor/dp/B01MXSJOAM/ref=pd_sbs_421_4/258-3304029-4666252?_encoding=UTF8&pd_rd_i=B01MXSJOAM&pd_rd_r=d8583cc7-c49c-4555-8458-922376152c88&pd_rd_w=OI7h8&pd_rd_wg=L7Ev0&pf_rd_p=f9384d3f-fa3d-4e25-8bc3-b0c7853cd8a6&pf_rd_r=NAPVMJNMWQ3GZRZT57FR&psc=1&refRID=NAPVMJNMWQ3GZRZT57FR"
    message = f"Subject : {subject}\n\n{body}"

    server.sendmail("xxxxx@gmail.com","xxxx@gmail.com",message)
    server.quit()
    print("Se ha enviado el el email")

def check_price():
    try:
        page = rq.get(URL, headers=header)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text()
        price = float(soup.find(id="priceblock_ourprice").get_text()[0:5])
        if price > 100 :
            send_email()
    except :
        print("Captcha")

check_price()


