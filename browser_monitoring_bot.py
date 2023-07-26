import time
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import csv

# Set Chrome executable path
chrome_exe_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# Initialize ChromeDriver
options = webdriver.ChromeOptions()
options.binary_location = chrome_exe_path

# Dictionary to store URL data
url_data = {}

def save_data(url):
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([url, url_data[url]['Domain'], url_data[url]['Unique ID'], url_data[url]['Time']])

def extract_data(url):
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Wait for the page to load (you may need to adjust the wait time based on the page)
        time.sleep(5)

        # Extract the domain from the URL
        domain = url.split('/')[2]

        # Extract the unique ID from the page (you may need to use a different element ID or CSS selector)
        try:
            unique_id_element = driver.find_element_by_id('unique_id')
            unique_id = unique_id_element.text if unique_id_element else "N/A"
        except NoSuchElementException:
            unique_id = "N/A"

        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        # Store the data in the url_data dictionary
        url_data[url] = {
            'Domain': domain,
            'Unique ID': unique_id,
            'Time': current_time
        }

        print(f"Domain: {domain}")
        print(f"Unique ID: {unique_id}")
        print(f"Time: {current_time}")
        print()

        driver.quit()

    except Exception as e:
        print(f"Error while extracting data for URL {url}: {e}")

def monitor_browser_urls():
    try:
        while True:
            # Get the current active window (browser window)
            active_window = gw.getActiveWindow()

            # Check if the window is a browser window and get its URL
            if active_window and "Google Chrome" in active_window.title:
                current_url = active_window.title
                if current_url:
                    if not current_url.startswith("http://") and not current_url.startswith("https://"):
                        print(f"Invalid URL format: {current_url}")
                        continue

                    if current_url not in url_data:
                        extract_data(current_url)
                        save_data(current_url)

            time.sleep(10)  # Check browser activity every 10 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_browser_urls()
