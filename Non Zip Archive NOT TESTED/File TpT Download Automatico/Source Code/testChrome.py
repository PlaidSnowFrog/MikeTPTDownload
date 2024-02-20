"""
Author: PlaidSnowFrog
Date: 3/12/2023
Description: This code downloads a file from Teachers Pay Teachers, that file shows the revenue.
"""

import subprocess
import os
import sys
import time
from datetime import datetime

print("DOWNLOADING TPT FILES, DO NOT CLOSE THIS WINDOW")

url = "https://www.teacherspayteachers.com/items/download_items_stats"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Make the name for the downloaded file
date = datetime.now()
formatted_date = date.strftime("%m%d%Y")  # Formats the date as MM/DD/YYYY
fileName = f"download  - {formatted_date}.csv"


# Download the file
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "TpT Downloads")
os.makedirs(downloads_folder, exist_ok=True)
file_path = os.path.join(downloads_folder, fileName)

subprocess.run([chrome_path, url])
time.sleep(5)

# Move the downloaded file from the default download location to the TpT Downloads directory
default_download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Check if the file exists in the default download folder<
default_download_file_path = os.path.join(default_download_folder, fileName)
if os.path.exists(default_download_file_path):
    # Move the file to the specified folder
    os.rename(default_download_file_path, file_path)


time.sleep(5)
sys.exit(0)