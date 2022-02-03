from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':


    url = "http://www.darklyrics.com/search?q=slayer+tormentor"

    # manually set the cookie before sending request
    cookies_dict = {"lastvisitts": str(52451002)}
    print("COOKIES DICTIONARY: " + str(cookies_dict))

    response = requests.get(url, cookies=cookies_dict)

    soup = BeautifulSoup(response.content, 'html.parser')
    sens = soup.find_all('div', class_='sen')
    print(sens)