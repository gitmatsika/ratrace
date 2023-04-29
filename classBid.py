import smtplib, ssl
import pandas as pd

from smtplib import SMTP
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime as dt
#import matplotlib.pyplot as plt

class Mybid:
    def __int__(self):
        pass
    def send_mail(self):
        pass

    def toCsv(self,bid):
        df = pd.DataFrame(bid)
        df.to_csv("../data/auction.csv", index=False)

    def readtolist(self):
        df = pd.read_csv('../data/auction.csv')
        auction = df.to_dict('records')
        return auction

    def checkEmail(self, email, auction):
        # check if email already exits for the bid
        found = False
        for d in auction:
            if d['email'] == email:
                # mytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
                found = True
                break
        return found

    def newbid(self, bid, email, name, amt):
        auctiondict = {}
        auctiondict['name'] = name
        auctiondict['amt'] = amt
        auctiondict['email'] = email
        mytime = dt.now().strftime("%m/%d/%Y")
        auctiondict['time'] = mytime
        if bid:
            highestBid = max(bid, key=lambda x: x['amt'])
            high = highestBid["amt"]
            bidExist = self.checkEmail(email,bid)
            if not bidExist:
                bid.append(auctiondict)
                if amt > high:
                    currency = "USD"
                    textp = f"Note that there is a new highest bid for {currency} {amt} at {mytime}"
                    textp = textp.title()
                    self.send_emails(textp, 22)
            else:
                print("You have already tendered a bid, you may want to change your bid price")
        else:
            bid.append(auctiondict)
        print(bid)
        return bid

    def send_emails(self, body, auctionNum):
        sub = f" Auction {auctionNum} Update"
        receiver = ["fmatsika@gmail.com"]
        # receiver = ["fmatsika@gmail.com"]
        subject = sub.title()
        body = body + "\n" + "\n" + "\n" + " Digital Metrics - Bringing Artificial Intelligence and Data Analytics into your daily operations"
        sender_email = "fmatsika@gmail.com"
        receiver_email = "fmatsika@epicicts.com"
        password ='rglpugqzzpikikml'
        #password = 'irsfniijrvpnathr'
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            for mail in receiver:
                server.sendmail(sender_email, mail, text)
        print("did we send mail")
    def amend(self, bid):
        #
        emailAdd = input("Please enter email address: ")
        newBid = int(input("Please enter new bid amount: "))
        match = None
        highestBid = max(bid, key=lambda x: x['amt'])
        high = highestBid["amt"]
        for d in bid:
            if d['email'] == emailAdd:
                mytime = dt.now().strftime("%m/%d/%Y")

                d.update({'amt': newBid, 'amendtime': mytime})
                if newBid > high:
                    currency = "USD"
                    textp = f"Take note, one of the bidders changed thier bid price to {currency} {newBid} at {mytime}"
                    textp = textp.title()
                    self.send_emails(textp, 22)

                break
