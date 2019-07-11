import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.com.au/Timberland-Premium-Boots-Black-Shoes/dp/B077PTB6NQ?pf_rd_p=de59ce98-c347-49f3-9378-1b23e39ccb2e&pd_rd_wg=Hsg1P&pf_rd_r=JTC5Z8YATDQV34F8NXKK&ref_=pd_gw_cr_simh&pd_rd_w=a4Ykz&pd_rd_r=acc1eef3-d0f1-40c7-8756-e34d33486683'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)
    title = soup.find(id="productTitle").get_text()
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 265):
        send_mail()
    
    
    if(converted_price > 265):
        send_mail()

    if(converted_price > 295.95):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib('smtp.gmail', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sirgoonythesecond@gmail.com', 'fddfdfd')

    subject = 'Price fell down!'
    body = 'Check he amazon link https://www.amazon.com.au/Timberland-Premium-Boots-Black-Shoes/dp/B077PTB6NQ?pf_rd_p=de59ce98-c347-49f3-9378-1b23e39ccb2e&pd_rd_wg=Hsg1P&pf_rd_r=JTC5Z8YATDQV34F8NXKK&ref_=pd_gw_cr_simh&pd_rd_w=a4Ykz&pd_rd_r=acc1eef3-d0f1-40c7-8756-e34d33486683'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('sirgoonythesecond@gmail.com', msg)
    print('yeeeeeeeee')
    server.quit()

    check_price()