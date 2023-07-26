# Real-Time Browser URL Monitor

This project is a Python script that uses Selenium to monitor multiple open browser tabs in real-time, extracts URL data (including domain and unique ID), and saves it to a CSV file. The script continuously checks for active browser tabs and captures the URL data when a valid URL is detected. The data is then stored in a CSV file for further analysis or tracking.

## Prerequisites

Before running the script, you need to install the required Python packages. You can install them using the following command:

```bash
pip install selenium pygetwindow pyperclip
```

Make sure you have Google Chrome installed on your system, as the script uses the Chrome browser to monitor the URLs.

## How to Use

1. Clone the repository to your local machine or download the `monitor_urls.py` file.

2. Make sure you have installed the required packages mentioned in the "Prerequisites" section.

3. Run the script using the following command:

```bash
python monitor_urls.py
```

4. The script will start monitoring the open browser tabs and capture URL data in real-time. The extracted data will be saved to a file named `data.csv`.

## Notes

- The script ignores URLs that do not start with "http://" or "https://" to avoid capturing invalid URLs.

- If a browser tab is closed while monitoring, the script will handle the error gracefully and continue monitoring other tabs.

- The script does not capture IP addresses as requested.

- The script continuously runs in the background until manually stopped by the user.

- The captured data includes the URL, domain, unique ID, and timestamp when the URL was first opened.

- The CSV file `data.csv` will be created in the same directory where the script is located.

- The script may require some modifications or fine-tuning based on your specific use case or browser configuration. Feel free to customize it as needed.

Enjoy monitoring and analyzing your browser URLs in real-time! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or contribute to the project. Happy coding!
