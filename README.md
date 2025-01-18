# price-comparision-tool
Overview
This script is designed to scrape product prices from three different e-commerce websites: Amazon, Flipkart, and Croma. It retrieves the price of the Samsung Galaxy S23 Ultra, stores the data for further analysis, and visualizes the price comparison using a bar chart.

Features

Scrapes product prices from Amazon, Flipkart, and Croma.
Stores scraped data in a binary file using pickle.
Reads and displays stored data.
Visualizes price comparison in a bar chart.

Requirements

To run this script, you need to have the following Python packages installed:

requests
beautifulsoup4
pandas
re
pickle
matplotlib
Installation
You can install the required packages using pip. Run the following command in your terminal:

pip install requests beautifulsoup4 pandas matplotlib

Usage

Set Up API Key: Replace the placeholder API key in the script with your own valid API key for the scraping service.

Run the Script: Execute the script in your Python environment. It will:

Scrape product data from Amazon, Flipkart, and Croma.
Store the scraped data in a binary file using pickle.
Read the stored data and print it to the console.
Visualize the price comparison in a bar chart.

View Results: After running the script, a bar chart will display the prices from each retailer.

Code Structure

Imports: The necessary libraries are imported at the beginning of the script.
Product URLs: URLs for the product on each e-commerce site are defined.
API Requests: The script makes GET requests to the scraping API for each product URL.
Data Extraction: It uses BeautifulSoup to parse the HTML and extract product titles and prices.
Data Storage: The extracted data is stored in a binary file using pickle.
Data Reading: A function to read and print the stored data is included.
Price Comparison: The script calculates the minimum price and visualizes the prices using a bar chart.

Important Notes
Ensure that you comply with the terms of service of the websites you are scraping.
The structure of the HTML on the e-commerce sites may change, which could break the scraping functionality. Adjust the class names in the soup.find() methods accordingly if needed.
This script is intended for educational purposes and should be used responsibly.

