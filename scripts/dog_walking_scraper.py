!pip install beautifulsoup4
!pip install requests

import requests
from bs4 import BeautifulSoup
import csv

# List of towns to scrape
towns = [
    "Beckenham", "Bromley", "Bickley", "Mottingham", "Sevenoaks",
    "Orpington", "Chislehurst", "Sidcup", "Dartford", "Tunbridge Wells"
]

# Open CSV file to write the results
with open('dog_walking_services.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Town', 'Service Name', 'Description'])  # Writing header

    # Loop through each town
    for town in towns:
        url = f"https://dogwalkerdirectory.co.uk/tag/{town.replace(' ', '-').lower()}/"  # Replace spaces with hyphens in URL
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the area name
            area_name = soup.find('div', class_='dwd-archive-search-under-title-locations').text.strip()

            # Extract service name
            service_name = soup.find('h1', class_='entry-title').text.strip()

            # Extract description
            description = soup.find('div', class_='entry-content').find('p').text.strip()

            # Write the data to the CSV file
            writer.writerow([area_name, service_name, description])
        else:
            print(f"Failed to retrieve data for {town}")

print("Scraping complete. Results saved in 'dog_walking_services.csv'.")
