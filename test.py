from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics
import requests
from bs4 import BeautifulSoup
import time, datetime
import math

if __name__ == '__main__':
    print(get_lyrics('Enemy', 'AS EDEN BURNS'))
    print("SUCCESSSSSSSSSSSs")
    print(get_lyrics('Ever Again', 'AS EDEN BURNS'))