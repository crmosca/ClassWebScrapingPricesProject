import httpx
from bs4 import BeautifulSoup
import csv
import pandas as pd
import asyncio
import os
import re

def clean_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

async def scrape_ebay_prices_and_names(search_term):
    ebay_url = f'https://www.ebay.com/sch/i.html?_nkw={search_term.replace(" ", "+")}'
    
    async with httpx.AsyncClient() as session:
        response = await session.get(ebay_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with class 's-item__info'
        item_elements = soup.find_all('div', class_='s-item__info')

        if not item_elements:
            print(f"No items found for '{search_term}' on eBay.")
            return

        # Extract and log the item listing names and prices
        data = []
        for index, item in enumerate(item_elements, start=1):
            title_element = item.find("div", class_="s-item__title")
            price_element = item.find('span', class_='s-item__price')

            name = title_element.get_text(strip=True) if title_element else f"Item {index} - No listing name available"
            price = price_element.get_text(strip=True) if price_element else f"Item {index} - No price available"

            data.append((name, price))
            print(f"Item {index} Listing Name: {name} | Price: {price}")

        # Get the absolute path for the CSV file
        directory = 'data/raw_data/'
        os.makedirs(directory, exist_ok=True)
        filename = clean_filename(f'{search_term}_ebay_prices_and_names.csv')
        csv_path = os.path.join(directory, filename)

        # Save names and prices to CSV
        df = pd.DataFrame(data, columns=['Listing Names', 'Prices'])
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Listing names and prices saved to {csv_path}")

if __name__ == "__main__":
    # Get user input for the search term
    search_term = input("Enter the product name that you want to search for on eBay: ")

    try:
        asyncio.run(scrape_ebay_prices_and_names(search_term))

    except httpx.RequestError as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
