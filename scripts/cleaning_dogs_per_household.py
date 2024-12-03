import pandas as pd

data = pd.read_csv('Dogs_Per_Household.csv')

print(data.info)
print(data.head)

data = data.dropna()

data['PostcodeDistrict'] = data['PostcodeDistrict'].str.upper()

data.to_csv('cleaned_dogs_per_household.csv', index=False)
