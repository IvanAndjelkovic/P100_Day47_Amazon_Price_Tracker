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





response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tag = soup.find('span', class_='a-offscreen')
full_price = tag.get_text()
price =float (full_price.split("$")[1])


if price<100:
    try:
        subject = 'Amazon Price Alert'
        body=f'Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now {full_price}\n{url}'
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





