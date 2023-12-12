import requests 
from bs4 import BeautifulSoup
import csv

#get user imput for the search term to search ebay for the product
search_term = input("Enter the product name that you want to search for: ")

#constructing the ebay URL with the user input in the search
url = f'https://www.ebay.com/sch/i.html?_nkw={search_term.replace(" ", "+")}'

#make the request to ebay
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

#find all of the prices on the page
prices = soup.find_all('span', class_='s-item__price')

if not prices:
    print(f"No prices found for '{search_term}' on ebay")
    
else:
    #print and save prices to a .csv 
    with open(f'data/raw_data/{search_term}_prices.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Price'])
        
        for price in prices:
            price_text = price.get_text(strip=True)
            print(price_text)
            csv_writer.writerow([price_text])

#create a way to deal with possible issues            
except requests.RequestException as e:
    print(f"Request failed: {e}")

except Exception as e:
    print(f"An unexpected error occured: {e}")