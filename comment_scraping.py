from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from datetime import datetime

# Configure Edge options
edge_options = Options()
edge_options.use_chromium = True
# Commenting out the headless mode for debugging purposes
# edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")

# Path to your Edge WebDriver
webdriver_path = 'edge/msedgedriver.exe'
service = EdgeService(webdriver_path)

# URL of the Bitcoin comments page
url = 'https://www.investing.com/crypto/bitcoin/chat'

# Start the WebDriver
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Function to handle "Verify you are human" checkbox
def verify_human(driver):
    try:
        # Wait for the "Verify you are human" checkbox to be present
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @id='recaptcha-anchor']"))
        )
        # Click the checkbox
        checkbox.click()
        print("Checked 'Verify you are human' checkbox.")
        time.sleep(5)  # Wait for the verification to complete
    except Exception as e:
        print(f"Error during human verification: {e}")

# Function to convert date strings to datetime objects
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%b %d, %Y, %H:%M')
    except ValueError:
        return datetime.strptime(date_str, '%b %d, %Y')

# Function to check if the date is older than the specified date
def is_older_than(date, year):
    return date.year < year

# Function to extract comments from the current page
def extract_comments():
    comments = driver.find_elements(By.CSS_SELECTOR, 'div.commentHolder')
    for comment in comments:
        try:
            content = comment.find_element(By.CSS_SELECTOR, 'div.text').text
            date_str = comment.find_element(By.CSS_SELECTOR, 'span.date').text
            published_date = parse_date(date_str)
            if is_older_than(published_date, 2012):
                return False  # Stop if we have reached comments older than 2012
            data.append({'content': content, 'published_date': published_date})
        except Exception as e:
            print(f"Error extracting comment: {e}")
            continue
    return True

# Scroll and load comments
data = []
page_number = 1
while True:
    print(f"Extracting comments from page {page_number}...")
    if not extract_comments():
        break

    # Check if there's a next page button and click it
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'hidden sm:block') and contains(text(), 'Next')]"))
        )
        print("Next button found. Clicking...")
        next_button.click()
        time.sleep(5)  # Wait for the next page to load
        page_number += 1
    except Exception as e:
        print(f"Error navigating to the next page: {e}")
        # Check for human verification
        if "Verify you are human" in driver.page_source:
            print("Human verification detected. Solving...")
            verify_human(driver)
        else:
            break

# Quit the WebDriver
driver.quit()

# Check if data is collected
if not data:
    print("No data collected. Please check the selectors and page structure.")
else:
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Print the DataFrame to debug
    print(df.head())

    # Convert published_date to datetime
    df['published_date'] = pd.to_datetime(df['published_date'])

    # Display the DataFrame
    print(df)

    # Save to a CSV file
    df.to_csv('bitcoin_comments.csv', index=False)
