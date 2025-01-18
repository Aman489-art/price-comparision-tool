
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import pickle 
import matplotlib.pyplot as plt 

api_key = "SCRAPING_ANT_API_KEY" 
#Get API KEY to use Scrapingant api service you can use another method 


product_url_amazon = "https://www.amazon.in/Samsung-Galaxy-Ultra-Green-Storage/dp/B0BT9CXXXX/ref=sr_1_1_sspa?nsdOptOutParam=true&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"
product_flipkart = "https://www.flipkart.com/samsung-galaxy-s23-ultra-5g-green-256-gb/p/itm77dc35f7779a4"
product_croma = "https://www.croma.com/samsung-galaxy-s23-ultra-5g-12gb-ram-256gb-green-/p/275154"

params = {
    "url": [
        product_url_amazon
    ]
}

params2 = {
    "url": [
        product_flipkart 
    ]
}

params3 = {
    "url": [
        product_croma

    ]
}

headers = {
    "x-api-key": api_key
}

r = requests.get("https://api.scrapingant.com/v2/general", params=params, headers=headers)

try:
    if r.status_code == 200:
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup.prettify())

        title = soup.find(class_="a-size-large product-title-word-break")
        product = title.text.strip()

        price = soup.find(class_="a-price-whole")
        amazon_price  = price.text.strip()

        #print(f"Amazon: {price.text.strip()}")


except Exception as e:
    print("Error extracting Amazon product data:", e)

r = requests.get("https://api.scrapingant.com/v2/general", params=params2, headers=headers)

try:
    if r.status_code == 200:
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup.prettify())

        price_flipkart = soup.find(class_="Nx9bqj CxhGGd")
        print(price_flipkart.text.strip())
        flipkart_price  = price_flipkart.get_text(strip=True)
        #print("Flipkart:" + price_flipkart.text.strip())

except Exception as e:
    print(e)

r = requests.get("https://api.scrapingant.com/v2/general", params=params3, headers=headers)

try:
    if r.status_code == 200:
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup.prettify())

        price_croma = soup.find(class_="amount")
        croma_price  = price_croma.text.strip()
        #print(f"Croma: {price_croma.text.strip()}")

except Exception as e:
    print(e)

def Store_Data():
    # Create a dictionary to store the data
    amazon = {'key' : 'amazon', 'product_name' : 'Samsung Galaxy S23 Ultra', 'price' : amazon_price}
    flipkart = {'key' : 'flipkart', 'product_name' : 'Samsung Galaxy S23 Ultra', 'price': flipkart_price}
    croma = {'key' : 'croma', 'product_name' : 'Samsung Galaxy S23 Ultra', 'price': croma_price}

    #database
    db = {}
    db['amazon'] = amazon
    db['flipkart'] = flipkart
    db['croma'] = croma

    # Its important to use binary mode
    dbfile = open('price_data', 'ab')
        
    # source, destination
    pickle.dump(db, dbfile)                    
    dbfile.close()

def read_data():
    # Open a file: file my_data in binary mode
    dbfile = open('price_data', 'rb')
    # dump the python object as a byte stream
    db = pickle.load(dbfile)
    for items in db:
        print(items, ' :: ', db[items])
    dbfile.close()

amazon_price = float(amazon_price.replace("₹", "").replace(",", ""))
flipkart_price = float(flipkart_price.replace("₹", "").replace(",", ""))
croma_price = float(croma_price.replace("₹", "").replace(",", ""))

min_price = min(amazon_price,flipkart_price,croma_price)


# Define the companies and prices
companies = ['Amazon', 'Flipkart', 'Croma']
prices = [amazon_price, flipkart_price, croma_price]

# Create the bar chart
plt.bar(companies, prices, color='blue')

# Add labels and title
plt.xlabel('Company')
plt.ylabel('Product Price (₹)')
plt.title('Product Price Comparison')

# Add labels to each bar
for i, v in enumerate(prices):
    plt.text(i, v + 3, str(v), color='black', ha='center')

# Show the chart
plt.show()
