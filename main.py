
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





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_lyrics('tormentor', 'slayer'))

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

#empty data frame
df = pd.DataFrame(columns = ['BAND', 'SONGS', 'ALL LYRICS'])

for i in range(10):
    try:
        print("BAND NAME: "+ band_list[i])

        darklyrics.get_albums(band_list[i])

        print("SONGS:")
        print(get_songs(band_list[i]))

        print("ALL LYRICS: ")
        print(get_all_lyrics(band_list[i]))

        df = df.append({'BAND': band_list[i], 'SONGS': get_songs(band_list[i]), 'ALL LYRICS': get_all_lyrics(band_list[i])},
                       ignore_index=True)






    except:
        print("Exception: Lyrics not found for "+band_list[i])
        df = df.append({'BAND': band_list[i], 'SONGS': 'Songs not found', 'ALL LYRICS':'Lyrics not found' }, ignore_index = True)




file_name ='test_a.xlsx'
  # saving the excel
df.to_excel(file_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
