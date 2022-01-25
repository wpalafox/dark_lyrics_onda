# This is a sample Python script.
import darklyrics
from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time
import pandas as pd

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.






def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Code to set up Chrome Driver
    url = "http://www.darklyrics.com/"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
    driver = webdriver.Chrome(executable_path=DRIVER_BIN)
    browser = driver.get(url)

    #will hold entire alphabet
    alpha = ['a']
    band_list = []

    for i in range(len(alpha)):


        # getting the button by class name
        letter_link = driver.find_element_by_xpath("//a[@href='/"+alpha[i]+".html']")

        # clicking on the button
        letter_link.click()

        #A_left_list = driver.find_elements(By.XPATH, "//div[@class='artists fl']//a")
        left_list = driver.find_elements_by_xpath("//div[@class='artists fl']//a")
        right_list = driver.find_elements_by_xpath("//div[@class='artists fr']//a")


        for j in range(len(left_list)):
            band_list.append(left_list[j].text)

        for j in range(len(right_list)):
            band_list.append(right_list[j].text)




#for band in band_list:
 #   print(band)

for i in range(len(band_list)):
    try:
        print("BAND NAME: "+ band_list[i])
        print("LYRICS:")
        print(get_all_lyrics(band_list[i]))

    except:
        print("lyrics not found")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
