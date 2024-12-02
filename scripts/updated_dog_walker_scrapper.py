!pip install beautifulsoup4
!pip install requests

import requests
from bs4 import BeautifulSoup
import csv

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
        page = 1
        while True:
            url = f"https://dogwalkerdirectory.co.uk/tag/{town.replace(' ', '-').lower()}/page/{page}/"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract the service details
                services = soup.find_all('article')
                if not services:
                    break  # Exit loop if no services found on the page

                # Loop through each service
                for service in services:
                    area_name = soup.find('div', class_='dwd-archive-search-under-title-locations').text.strip()
                    service_name = service.find('h1', class_='entry-title').text.strip()
                    description = service.find('div', class_='entry-content').find('p').text.strip()

                    writer.writerow([area_name, service_name, description])

                page += 1  # Go to next page
            else:
                break  # Stop if no response from the page

print("Scraping complete. Results saved in 'dog_walking_services.csv'.")
