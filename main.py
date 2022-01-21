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

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']




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

    # getting the button by class name
    A_link = driver.find_element_by_xpath("//a[@href='/a.html']")

    # clicking on the button
    A_link.click()

    #A_left_list = driver.find_elements(By.XPATH, "//div[@class='artists fl']//a")
    A_left_list = driver.find_elements_by_xpath("//div[@class='artists fl']//a")

    for i in range(len(A_left_list)):
        print(A_left_list[i].text)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
