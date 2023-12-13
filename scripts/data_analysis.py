import pandas as pd
import re

def clean_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

# Get user input for the search term
search_term = input("Enter the product name that you want to search for on eBay: ")

# Loading the data from the CSV file
cleaned_search_term = clean_filename(search_term)
csv_file_path = f'data/raw_data/{cleaned_search_term}_ebay_prices_and_names.csv'
ebay_data = pd.read_csv(csv_file_path)

# Data cleaning: convert 'Prices' column to numeric, get rid of non-numeric symbols, handle ranges
ebay_data['Prices'] = ebay_data['Prices'].replace('[\$,]', '', regex=True)
# Handling cases like '2.00to79.00' by taking the average of the range
ebay_data['Prices'] = ebay_data['Prices'].apply(lambda x: (float(x.split('to')[0]) + float(x.split('to')[1])) / 2 if 'to' in x else float(x))

# Calculating average price for each listing on eBay
average_price_per_listing_ebay = ebay_data.groupby('Listing Names')['Prices'].mean()

# Display results
print(f"Analysis for search term: {search_term}")

print("\nAnalysis for eBay:")
print("\nAverage Price for Each Listing (eBay):")
print(average_price_per_listing_ebay)
