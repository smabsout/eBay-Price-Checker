import requests   #allows you to get data from a website -- eg. a specific product from amazon
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.ebay.com/itm/Nintendo-Switch-Lite-Gray-Yellow-Turquoise-New/264562227254?hash=item3d99233836:g:8DkAAOSwKp1d7xPf:sc:FedExHomeDelivery!77095!US!-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'} #gets information about our browser


def price_check():
    page = requests.get(URL, headers=headers) #this returns all data from the website, in this case ebay

    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="itemTitle").get_text()
    price = (soup.find(id="prcIsum").get_text())
    converted_price = float(price[4:9])

    print(title.strip())
    print (converted_price)
   
   
    if(converted_price > 250.00):
        print("Item is on Sale! :)")
        send_mail()
    else:
        print("Price is still too high! :(")

    print('----------------------------\n')

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() #encrypts connection
    server.ehlo()

    server.login('smabsout@gmail.com',"wcmumjtbxorouxnj")

    subject = 'Human! The price fell down!'
    body = 'The Price fell down on the nintendo switch!\n check the link: https://www.ebay.com/itm/Nintendo-Switch-Lite-Gray-Yellow-Turquoise-New/264562227254?hash=item3d99233836:g:8DkAAOSwKp1d7xPf:sc:FedExHomeDelivery!77095!US!-1 '
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'smabsout@gmail.com',
        'smabsout1993@outlook.com',
        msg
    )

    print('EMAIL SENT!')

    server.quit()

price_check()
