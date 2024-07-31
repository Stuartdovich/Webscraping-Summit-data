from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL of the webpage
url = "https://www.aimsummit.com/event/dubai/websitePage:b620da85-d6d6-4f4b-99cd-7b81ce616c1f"
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust based on your connection speed and page load time

# Create a list to store investor data
investors = []

# Find all speaker cards
speaker_cards = driver.find_elements(By.CLASS_NAME, 'SpeakersStyles__speakerCardContent___a34b')

for card in speaker_cards:
    try:
        # Extract name
        name_element = card.find_element(By.XPATH, './/h3[@class="css-87ndg2"]')
        name_parts = name_element.text.split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:])
        
        # Click the "View Profile" button
        view_profile_button = card.find_element(By.XPATH, './/button[@title="View Profile"]')
        view_profile_button.click()
        
        # Wait for the profile modal to load (adjust time as needed)
        time.sleep(5)
        
        # Extract LinkedIn profile and other details from the modal
        linkedin = ""
        location = ""
        
        try:
            linkedin_element = driver.find_element(By.XPATH, '//a[contains(@href, "linkedin.com")]')
            linkedin = linkedin_element.get_attribute('href')
        except Exception as e:
            print(f"LinkedIn profile not found: {e}")
        
        try:
            location_element = driver.find_element(By.XPATH, '//div[@class="SpeakersStyles__speakerModalBiography___a34b"]')
            location = location_element.text  # Adjust if necessary to extract specific location details
        except Exception as e:
            print(f"Location not found: {e}")
        
        investors.append({
            'First Name': first_name,
            'Last Name': last_name,
            'LinkedIn': linkedin,
            'Location': location
        })

        # Close the modal or navigate back if necessary
        close_button = driver.find_element(By.ID, 'closeButton')
        close_button.click()
        time.sleep(3)  # Adjust based on the time it takes to close the modal

    except Exception as e:
        print(f"Error processing card: {e}")

# Close the WebDriver
driver.quit()

# Convert to DataFrame and save to CSV
df = pd.DataFrame(investors)
df.to_csv('investors_list_with_location.csv', index=False)

print("Data has been saved to investors_list_with_location.csv")
