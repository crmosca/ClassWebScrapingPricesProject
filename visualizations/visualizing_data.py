import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

def clean_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

# Get user input for the search term
search_term = input("Enter the product name that you want to visualize on eBay: ")

# Clean the search term for filename
cleaned_search_term = clean_filename(search_term)

# Construct the absolute file path
script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_directory, f'../data/raw_data/{cleaned_search_term}_ebay_prices_and_names.csv')

# Load the data from the CSV file
ebay_data = pd.read_csv(csv_file_path)

# Convert 'Prices' column to numeric
ebay_data['Prices'] = ebay_data['Prices'].replace('[\$,]', '', regex=True).astype(float)

# Creating a boxplot for eBay data
plt.figure(figsize=(10, 6))
sns.boxplot(x='Listing Names', y='Prices', data=ebay_data)
plt.title('Boxplot of Prices for eBay Data')
plt.xticks(rotation=90)
plt.show()

# Creating a violin plot for Prices with Listing Names
plt.figure(figsize=(12, 6))
sns.violinplot(x='Listing Names', y='Prices', data=ebay_data, inner='quartile', cut=0)
plt.title('Violin Plot of Prices for eBay Data')
plt.xticks(rotation=90)
plt.xlabel('Listing Names')
plt.ylabel('Prices')
plt.show()

# Creating a FacetGrid of KDE plots for each Listing Name
g = sns.FacetGrid(ebay_data, col='Listing Names', col_wrap=4, height=4, sharex=False, sharey=False)
g.map(sns.kdeplot, 'Prices', fill=True)
g.set_axis_labels('Prices', 'Density')
g.set_titles(col_template="{col_name}")
plt.show()

# Print basic statistical data
statistical_data = ebay_data['Prices'].describe().to_frame().transpose()
print("\nStatistical Data for Prices:")
print(statistical_data)
