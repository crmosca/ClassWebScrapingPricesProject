import requests 
from bs4 import BeautifulSoup
import csv

#get user imput for the search term to search ebay for the product
search_term = input("Enter the product name that you want to search for: ")

#constructing the ebay URL with the user input in the search
ebay_url = f'https://www.ebay.com/sch/i.html?_nkw={search_term.replace(" ", "+")}'

#now amazon as well 
amazon_url = f'https://www.amazon.com/s?k={search_term.replace(" ", "+")}'

#and google shopping too
google_shopping_url = f'https://www.google.com/shopping?q={search_term.replace(" ", "+")}'

#define the requests to the specified URL 
def scrape_prices_and_details(url, site_name):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #find and retrieve the listing names
    listings = soup.find_all('div', class_='s-title-instructions') if 'ebay' in site_name else soup.find_all('span', class_='a-text-normal') if 'amazon' in site_name else soup.find_all,('h3', class_='product-title')

    #find all of the prices on the listings
    prices = soup.find_all('span', class_='s-item__price') if 'ebay' in site_name else soup.find_all('span', class_='a-offscreen') if 'amazon' in site_name else soup.find_all('span', class_='currency-value')
    
    #find all of the brand-names on the listings
    brands = soup.find_all('span', class_='s-item__dynamic s-item__brand') if 'ebay' in site_name else soup.find_all('span', class_='a-text-brand') if 'amazon' in site_name else soup.find_all('span', class_='brand')

    if not prices:
        print(f"No prices found for '{search_term}' on {site_name.capitalization()}.")
    
    else:
        #print and save data to a .csv 
        with open(f'data/raw_data/{search_term}_prices.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Listing Name', 'Price', 'Brand'])
        
        for listing, price, brand in zip(listings, prices, brands):
            listing_name=listing.get.text(strip=True) if 'ebay' in site_name else listing.get_text(strip=True) if 'amazon' in site_name else listing.get_text(strip=True)
            price_text = price.get_text(strip=True)
            brand_name = brand.get_text(strip=True) if 'ebay' in site_name else brand.get_text(strip=True) if 'amazon' in site_name else brand.get_text(strip=True)
            print(f"Listing: {listing_name}, Price: {price_text}, Brand: {brand_name}")
            csv_writer.writerow([listing_name, price_text, brand_name])

#create a way to deal with possible issues            
except requests.RequestException as e:
    print(f"Request failed: {e}")

except Exception as e:
    print(f"An unexpected error occured: {e}")

#scraping prices and details for ebay
scrape_prices_and_details(ebay_url, 'ebay')

#scrape prices for amazon
scrape_prices_and_details(amazon_url, 'amazon')

#scrape prices for google shopping
scrape_prices_and_details(google_shopping_url, 'google_shopping')