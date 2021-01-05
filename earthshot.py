import requests
from selenium import webdriver
import time
import csv

zoom = "6970.04703957d"

def earthshot():
    f = open("coordinates.csv")
    csv_f = csv.reader(f)

    for coords in csv_f:
        coords = "".join(coords)
        url = "https://earth.google.com/web/@" + coords + "," + zoom
        DRIVER = 'chromedriver'
        driver = webdriver.Chrome(DRIVER)
        driver.get(url)
        time.sleep(6)
        screenshot = driver.save_screenshot(coords + '.png')
        driver.quit()
        print("Screenshot saved for " + coord + "!")

earthshot()
