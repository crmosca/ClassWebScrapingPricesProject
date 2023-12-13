import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

def clean_filename(filename):
    #removing invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

#getting user input for the search term
search_term = input("Enter the product name that you want to visualize from eBay (make sure you write it exactly the same way): ")

#cleaning the search term for filename
cleaned_search_term = clean_filename(search_term)

#constructing the absolute file path
script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_directory, f'../data/raw_data/{cleaned_search_term}_ebay_prices_and_names.csv')

#loading the data from the CSV file
ebay_data = pd.read_csv(csv_file_path)

#converting 'Prices' column to numeric
ebay_data['Prices'] = ebay_data['Prices'].replace('[\$,]', '', regex=True).astype(float)

#creating a boxplot for eBay data
plt.figure(figsize=(10, 6))
sns.boxplot(x='Listing Names', y='Prices', data=ebay_data)
plt.title('Boxplot of Prices for eBay Data')
plt.xticks(rotation=90)
plt.show()

#creating a violin plot for Prices with Listing Names
plt.figure(figsize=(12, 6))
sns.violinplot(x='Listing Names', y='Prices', data=ebay_data, inner='quartile', cut=0)
plt.title('Violin Plot of Prices for eBay Data')
plt.xticks(rotation=90)
plt.xlabel('Listing Names')
plt.ylabel('Prices')
plt.show()

#printing basic statistical data
statistical_data = ebay_data['Prices'].describe().to_frame().transpose()
print("\nStatistical Data for Prices:")
print(statistical_data)
