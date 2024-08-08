import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# URL for the webpage
url = 'https://hprera.nic.in/PublicDashboard'

# Set up the webdriver
driver = webdriver.Safari()  # or webdriver.Chrome()

# Navigate to the webpage
driver.get(url)

# Get the HTML content after JavaScript execution
html = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all project entries
project_entries = soup.find_all('div', class_='shadow py-3 px-3 font-sm radius-3 mb-2')

# Create a list to store project details
project_details = []

# Loop through each project entry
for entry in project_entries:
    project = {}
    rera_link = entry.find('div', class_='').find('a', title='View Application')
    if rera_link:
        print(rera_link)
        detail_url = 'https://hprera.nic.in/PublicDashboard'
        driver.get(detail_url)
        detail_html = driver.page_source
        detail_soup = BeautifulSoup(detail_html, 'html.parser')
        project['GSTIN No'] = detail_soup.find('td', class_='mr-1 fw-600').text.strip()
        project['PAN No'] = detail_soup.find('td', class_='mr-1 fw-600').text.strip()
        project['Name'] = detail_soup.find('td', class_='fw-600').text.strip()
        project['Permanent Address'] = detail_soup.find('td', class_='fw-600').text.strip()
        project_details.append(project)

# Create a Pandas DataFrame
df = pd.DataFrame(project_details)

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('registered_projects.csv', index=False)
