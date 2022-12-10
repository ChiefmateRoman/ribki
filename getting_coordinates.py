from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class Getting_coordinates:
    def __init__(self, imo):
        self.imo = imo

    def getting_coordinates(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"https://www.vesselfinder.com/vessels/details/{self.imo}")

        upcoming_events_ul = driver.find_element(By.CLASS_NAME, 'text2')

        upcoming_events_text = upcoming_events_ul.text

        list = upcoming_events_text.split("coordinates")
        join_list = "".join(list[1])
        coordinates_text = join_list.split(") reported")
        lat_long = ''.join(coordinates_text[0])
        latitude_longitude = lat_long.split("/")
        latitude = float(latitude_longitude[0].split()[0])
        longitude = float(latitude_longitude[1].split()[0])
        top = round((69.62417-latitude)*1147.27)
        left = round(1334-(35.59167-longitude)*368.3896)
        return(top, left)

