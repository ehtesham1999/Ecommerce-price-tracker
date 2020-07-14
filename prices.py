import requests as r
from bs4 import BeautifulSoup as bs
import time
import webbrowser as w
import smtplib

def send_email():
    sender = "ehteshamhussain1999@gmail.com"
    receiver = "ehussain414@gmail.com"

    message = "realme 6 is available"
    s =  smtplib.SMTP(sender,587)
    s.starttls()
    s.login(sender,"yourballsareinmyfist")
    s.sendmail(sender,receiver,message)
    s.quit()




URL = "https://www.flipkart.com/realme-6-comet-blue-128-gb/p/itm64975b00cb8e6?pid=MOBFPCX7UQU3CHKG&lid=LSTMOBFPCX7UQU3CHKG2J1SAU&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=1aef97f8-7ea0-4228-ad1f-0ea5129c2d04.MOBFPCX7UQU3CHKG.SEARCH&ppt=sp&ppn=sp&ssid=yfp1st24g00000001592410182089&qH=ba2b1763f76b622e"
send_email()

while True:
    page = r.get(URL)
    soup = bs(page.content, "html.parser")
    available = "default"
    # Use whatever you see in Inspect Element of the website this keeps changing from web page to webpage
    available = soup.find("div", {"class": "_9-sL7L"}).text

    # Conver the price which is string to an integer to compare
    print(available)

    # Use your comparing logic here below
    # Example:
    if available != "Sold Out":
        w.open(URL)
        send_email()
        break
    else:
        print("Unavailable")

    # Any time you want it to wait to check next time. I gave 5 seconds
    time.sleep(5)
