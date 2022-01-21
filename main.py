# This is a sample Python script.
import darklyrics
from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics
import selenium
from selenium import webdriver
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
