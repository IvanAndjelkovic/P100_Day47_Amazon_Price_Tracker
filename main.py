import requests
from bs4 import BeautifulSoup
import os 
import dotenv
import smtplib



url = "https://appbrewery.github.io/instant_pot/"

smtp_address = dotenv.get_key('.env', 'SMTP_ADDRESS')
email_address = dotenv.get_key('.env', 'EMAIL_ADDRESS')
email_password = dotenv.get_key('.env', 'EMAIL_PASSWORD')
email_to ='viketbre@gmail.com'
url_real = "https://www.amazon.de/dp/B0CNH8MS16"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}






response = requests.get(url=url_real, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# Preissuche (verschiedene mögliche Selektoren)
# price_element = soup.select_one('span.a-offscreen')
# if price_element:
#     price_text = price_element.get_text()
#     print(f"Gefundener Preis: {price_text}")
# else:
#     print("Preis nicht gefunden")


# tag = soup.find_all('div', class_='a-spacing-top-mini')
# print(tag)
# full_price = tag.get_text()
# price =float (full_price.split("$")[1])
# print(price)
price =101
if price<100:
    try:
        subject = 'Amazon Price Alert'
        body=f'Lenovo-Tablet-Display-MediaTek-Android is now {full_price}\n{url}'
        message=f'Subject: {subject}\n\n{body}'
        with smtplib.SMTP(smtp_address,587) as connection:
            connection.starttls()
            connection.login(user=email_address, password = email_password)
            connection.sendmail(
                from_addr=email_address,
                to_addrs=email_to,
                msg=message.encode('utf-8')
            )
        print(f"Email sent successfully to {email_to}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")





