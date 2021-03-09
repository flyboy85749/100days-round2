import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = [YOUR EMAIL]
MY_PASSWORD = [YOUR PASSWORD]

url = [YOUR URL]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(url=url,
                        headers=headers)
site_html = response.content
soup = BeautifulSoup(site_html, "lxml")
# print(soup.prettify())

price = (soup.find(id="priceblock_ourprice"))
price_string = price.get_text().replace("$", "")
if "," in price_string:
    price = float(price_string.replace(",", ""))
else:
    price = float(price_string)
    print(price)

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 300

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=SEND_EMAIL_ADDRESS,
            to_addrs=TO_EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

