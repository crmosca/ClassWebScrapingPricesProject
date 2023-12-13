import pandas as pd
import re

def clean_filename(filename):
    #removing invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

#getting user input for the search term
search_term = input("Enter the product name that you searched for on eBay (make sure you write it exactly the same way): ")

#loading the data from the CSV file
cleaned_search_term = clean_filename(search_term)
csv_file_path = f'data/raw_data/{cleaned_search_term}_ebay_prices_and_names.csv'
ebay_data = pd.read_csv(csv_file_path)

#data cleaning: convert 'Prices' column to numeric, get rid of non-numeric symbols, handle ranges
ebay_data['Prices'] = ebay_data['Prices'].replace('[\$,]', '', regex=True)
#handling cases like '2.00to79.00' by taking the average of the range
ebay_data['Prices'] = ebay_data['Prices'].apply(lambda x: 
                                                (float(x.split('to')[0]) + float(x.split('to')[1])) / 2 
                                                if isinstance(x, str) and 'to' in x else float(x))

#cleaning the listing names by removing special characters
ebay_data['Listing Names'] = ebay_data['Listing Names'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

#saving the cleaned data back to the CSV file
ebay_data.to_csv(csv_file_path, index=False)

#calculating average price for each listing on eBay
average_price_per_listing_ebay = ebay_data.groupby('Listing Names')['Prices'].mean()

#displaying results
print(f"Analysis for search term: {search_term}")

print("\nAnalysis for eBay:")
print("\nAverage Price for Each Listing (eBay):")
print(average_price_per_listing_ebay)
