#Installing and loading pandas
!pip install pandas
import pandas as pd

#Loading datasets
dogdata = pd.read_csv('cleaned_dogs_per_household.csv')
walkingdata = pd.read_csv('cleaned_dog_walking_services.csv')

# Grouping by town and summing the number of dogs per household
dogs_per_town = dogdata.groupby('town')['dogs'].sum()

# Display the result
print(dogs_per_town)

# List of towns you're interested in
towns_of_interest = ['beckenham', 'bromley', 'bickley', 'mottingham', 'sevenoaks', 
                     'orpington', 'chislehurst', 'sidcup', 'dartford', 'tunbridge Wells', 
                     'bellingham', 'lee']

# Loop through each town in towns_of_interest
for town in towns_of_interest:
    filtered_services = walkingdata[walkingdata['Town'].str.contains(town, case=False, na=False)]
    
    # Count the number of services for each town
    service_count = filtered_services['Service Name'].count()
    print(f'Town: {town}, Services Available: {service_count}')

#combining data into a new table (used ai for help)

# Create a list to store the results
combined_data = []

# Loop through each town in towns_of_interest
for town in towns_of_interest:
    # Get the dog data for the town
    dog_count = dogs_per_town.get(town.lower(), 0)
    
    # Get the service data for the town
    filtered_services = walkingdata[walkingdata['Town'].str.contains(town, case=False, na=False)]
    service_count = filtered_services['Service Name'].count()

    # Append the data to the list
    combined_data.append({'Town': town, 'Dogs Available': dog_count, 'Services Available': service_count})

# Convert the list into a DataFrame
combined_df = pd.DataFrame(combined_data)

# Save the DataFrame to a new CSV file
combined_df.to_csv('combined_dog_data.csv', index=False)

print('Combined data saved to combined_dog_data.csv')

