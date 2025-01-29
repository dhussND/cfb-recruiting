#!/usr/bin/env python3

import json

file = open('names.txt', 'r')

# List of URLs to process
player_to_url = {}

for line in file:
    line = line.strip()[3:] + " }"
    line = json.loads(line)
    # print(line)
    # print(f"{line['name']}: {line['sameAs']}")
    player_to_url[line["name"]] = line["sameAs"]
    # print(type(line))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no browser UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Update with the path to your ChromeDriver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

offers_url = {}

# Iterate through each URL
for player in player_to_url:
    url = player_to_url[player]
    try:
        # Open the URL
        driver.get(url)
        time.sleep(1)  # Wait for the page to load (adjust if necessary)

        # Find the "see all recruiting offers" link and click it
        try:
            link = driver.find_element(By.LINK_TEXT, "View recruiting profile")
            link.click()
            link = driver.find_element(By.LINK_TEXT, "View complete team list")
        except:
            link = driver.find_element(By.LINK_TEXT, "View complete team list")
        
        link.click()
        time.sleep(1)  # Optional: Wait after clicking (adjust as needed)

        current_url = driver.current_url
        print(f"Current URL after clicking: {current_url}")
        offers_url[player] = current_url

        # Do something after clicking, if necessary (e.g., scrape data, save info)

    except Exception as e:
        print(f"{player}: Error processing {url}: {e}")

# Quit the browser
driver.quit()

print(offers_url)
