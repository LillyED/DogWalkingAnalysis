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

#Saving the clean data
data.to_csv('cleaned_dogs_per_household.csv', index=False)
