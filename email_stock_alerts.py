


import pandas as pd #data manipulation and analysis package
from alpha_vantage.timeseries import TimeSeries #enables data pull from Alpha Vantage

import time
import smtplib #enables you to send emails




#Getting the data from alpha_vantage
ts = TimeSeries(key='7R5HTNHSODF74G1Y', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
#We are currently interested in the latest price
close_data = data['4. close'] #The close data column
last_price = close_data[0] #Selecting the last price from the close_data column
#Check if you're getting a correct value
print(last_price)
#Set the desired message you want to see once the stock price is at a certain level
sender_email = "lidget987@gmail.com" #The sender email
rec_email = "caliverp123@hotmail.com" #The receiver email
password = ("Qwjhbnwzzxqowahk")#The password to the sender email
message = "MSFT STOCK ALERT!!! The stock is at above price you set " + "%.6f" % last_price #The message you want to send
target_sell_price = 220 #enter the price you want to sell at
if last_price > target_sell_price:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('lidget987@gmail.com', 'Qwjhbnwzzxqowahk') #logs into your email account
    print("Login Success")#confirms that you have logged in succesfully
    server.sendmail('lidget987@gmail.com', 'caliverp123@hotmail.com', 'Lock you')#send the email with your custom mesage
    print("Email was sent") #confirms that the email was sent







