#Install and load the data
!pip install pandas
import pandas as pd
data = pd.read_csv('dog_walking_services.csv')

#Inspect the data
print(data.info)
print(data.head)

#Cleaning the data
data = data.dropna()  

data['Town'] = data['Town'].str.lower()

data = data.drop_duplicates()

data['Service Name'] = data['Service Name'].str.strip()

#Saving the clean data
data.to_csv('cleaned_dog_walking_services.csv', index=False)
