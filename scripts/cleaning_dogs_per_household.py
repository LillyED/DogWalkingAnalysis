#Install and load the data
!pip install pandas
import pandas as pd
data = pd.read_csv('Dogs_Per_Household.csv')

#Inspect the data
print(data.info)
print(data.head)

#Cleaning the data
data = data.dropna()

data['PostcodeDistrict'] = data['PostcodeDistrict'].str.upper()

#Changing column names to make coding easier
data = data.rename(columns={'PostcodeDistrict': 'postcode', 'DogsPerHousehold': 'dogs'})

# Mapping postcodes to towns (used ai to help with this part)
postcode_to_town = {
    'BR3': 'beckenham', 'BR1': 'bromley', 'BR2': 'bromley', 'SE9': 'mottingham',
    'TN13': 'sevenoaks', 'TN14': 'sevenoaks', 'TN15': 'sevenoaks', 'BR5': 'orpington',
    'BR6': 'orpington', 'BR7': 'chislehurst', 'SE12': 'lee', 'SE6': 'bellingham',
    'DA14': 'sidcup', 'DA15': 'sidcup', 'DA1': 'dartford', 'DA2': 'dartford',
    'TN1': 'tunbridge wells', 'TN2': 'tunbridge wells', 'TN3': 'tunbridge wells', 'TN4': 'tunbridge wells'
}

# Function to map postcodes to towns (used ai to help with this part)
data['town'] = data['postcode'].apply(lambda x: next((town for code, town in postcode_to_town.items() if str(x).startswith(code)), 'unknown'))

# Remove rows where 'town' is 'unknown'
data = data[data['town'] != 'unknown']

#Saving the clean data
data.to_csv('cleaned_dogs_per_household.csv', index=False)
