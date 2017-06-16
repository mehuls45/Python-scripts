#! python3
# youtube_views.py - simple python scripts to get more views
# for youtube videos

import time
from selenium import webdriver

count = int(input("Number of times to be repeated: "))

url = input("Enter the URL of the video(no https): ")
print( "Length of video")
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

refreshrate = minutes * 60 + seconds

driver = webdriver.Firefox()
driver.get("http://"+url)

for x in range(count):
    time.sleep(refreshrate)
    driver.refresh()

print('Done')
