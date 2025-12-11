from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

# Connect to Website and pull in data

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1' # Example URL of an Amazon product

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} # Headers to mimic a browser visit

page = requests.get(URL, headers=headers) # Send a GET request to the URL with the specified headers

soup1 = BeautifulSoup(page.content, "html.parser") # Parse the content of the page with BeautifulSoup

soup2 = BeautifulSoup(soup1.prettify(), "html.parser") # Prettify the parsed content and parse it again with BeautifulSoup

title = soup2.find(id='productTitle').get_text() # Find the product title by its HTML element ID

price = soup2.find(id='priceblock_ourprice').get_text() # Find the product price by its HTML element ID

print(title)
print(price)



# Clean up the data a little bit

price = price.strip()[1:] # Remove whitespace and the dollar sign from the price
title = title.strip() # Remove whitespace from the title

print(title)
print(price)



# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today() # Get today's date

print(today)



import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f: # Open the CSV file in write mode
    writer = csv.writer(f) # Create a CSV writer object 
    writer.writerow(header) # Write the header row
    writer.writerow(data) # Write the data row
    
import pandas as pd

df = pd.read_csv(r'C:\Users\user\AmazonWebScraperDataset.csv') 

print(df)
#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f: # Open the CSV file in append mode
    writer = csv.writer(f) # Create a CSV writer object
    writer.writerow(data) # Write the data row again to append it
#Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1' # Example URL of an Amazon product

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='priceblock_ourprice').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
 
    
# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)



# If you want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it

df = pd.read_csv(r'C:\Users\alexf\AmazonWebScraperDataset.csv')

print(df)
# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('sowmya511n@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "sowmya, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sowmya511n@gmail.com',
        msg
     
    )