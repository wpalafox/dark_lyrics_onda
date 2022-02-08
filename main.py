
import darklyrics
from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
import random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.





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

#empty data frame
df = pd.DataFrame(columns = ['BAND', 'SONG', 'LYRICS'])

for i in range(len(band_list)):
    try:
        print("BAND NAME: "+ band_list[i])



        print("SONGS:")
        print(get_songs(band_list[i]))

        song_list = get_songs(band_list[i])

        for j in range(len(song_list)):
            try:
                df = df.append({'BAND': band_list[i], 'SONG': song_list[j], 'LYRICS': get_lyrics(song_list[j], band_list[i])},
                       ignore_index=True)
                print(get_lyrics(song_list[j], band_list[i]))
                time.sleep(random.randint(2,5))
            except:
                df = df.append(
                    {'BAND': band_list[i], 'SONG': song_list[j], 'LYRICS': 'Lyrics not found'},
                    ignore_index=True)
                print('LYRICS NOT FOUND FOR: '+song_list[j]+' by '+ band_list[i])
                time.sleep(random.randint(2, 5))







    except:
        print("Exception: Lyrics not found for "+band_list[i])
        df = df.append({'BAND': band_list[i], 'SONGS': 'Songs not found', 'LYRICS':'Lyrics not found' }, ignore_index = True)




file_name ='test_a.xlsx'
  # saving the excel
df.to_excel(file_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
