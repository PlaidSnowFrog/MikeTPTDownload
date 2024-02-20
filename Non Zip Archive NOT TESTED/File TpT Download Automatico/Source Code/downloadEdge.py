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
from urllib import response

print("DOWNLOADING TPT FILES, DO NOT CLOSE THIS WINDOW")

url = "https://www.teacherspayteachers.com/items/download_items_stats"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Make the name for the downloaded file
date = datetime.now()
formatted_date = date.strftime("%m%d%Y")  # Formats the date as MM/DD/YYYY
fileName = f"download  - {formatted_date}.csv"

# Get the date
# Check if the script has not already run on the first day of the month
log_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "last_execution_log.txt")
last_execution_date = None


try:
    with open(log_file_path, "r") as log_file:
        last_execution_date = datetime.strptime(log_file.read().strip(), "%Y-%m-%d")
except FileNotFoundError:
    pass  # The log file doesn't exist, so it's the first run

if last_execution_date is None or last_execution_date.day != date.day:
    # Download the file

    subprocess.run([edge_path, url])
    time.sleep(5)

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "TpT Downloads")
    
    # Ensure the directory exists; create it if not
    os.makedirs(downloads_folder, exist_ok=True)
    
    # Specify the full path for the downloaded file
    file_path = os.path.join(downloads_folder, fileName)
    
    with open(file_path, "wb") as f:
        f.write(response.content)


    # Update the last execution log
    with open(log_file_path, "w") as log_file:
        log_file.write(date.strftime("%Y-%m-%d"))



# Make the code run at startup
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    with open(os.path.join(bat_path, "DownloadTpT.bat"), "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)

# Check if the .bat file for startup already exists
def is_startup_script_added():
    startup_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "DownloadTpT.bat")
    return os.path.isfile(startup_path)

if not is_startup_script_added():
    add_to_startup()



sys.exit(0)