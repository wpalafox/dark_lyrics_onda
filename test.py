from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics
import requests
from bs4 import BeautifulSoup
import time, datetime
import math

if __name__ == '__main__':
    #calculate cookie value here
    def now_milliseconds():
        return int(time.time() * 1000)

    # reference time.time
    # Return the current time in seconds since the Epoch.
    # Fractions of a second may be present if the system clock provides them.
    # Note: if your system clock provides fractions of a second you can end up
    # with results like: 1405821684785.2
    # our conversion to an int prevents this

    def date_time_milliseconds(date_time_obj):
        return int(time.mktime(date_time_obj.timetuple()) * 1000)

    mstimeone = now_milliseconds()
    mstimetwo = date_time_milliseconds(datetime.datetime.utcnow())
    lastvisitts = str(math.ceil(mstimetwo / (60 * 60 * 6 * 1000)))
    lastvisittscookie = 0

    for i in range(len(lastvisitts)):
        lastvisittscookie = ((lastvisittscookie << 5) - lastvisittscookie) + ord(lastvisitts[i])
        lastvisittscookie = lastvisittscookie & lastvisittscookie


    url = "http://www.darklyrics.com/search?q=A-I-E-A+Diaphanous"

    # manually set the cookie before sending request
    cookies_dict = {"lastvisitts": str(lastvisittscookie)}
    print("COOKIES DICTIONARY: " + str(cookies_dict))

    response = requests.get(url, cookies=cookies_dict)

    soup = BeautifulSoup(response.content, 'html.parser')
    sens = soup.find_all('div', class_='sen')
    print(sens)