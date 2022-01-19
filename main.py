# This is a sample Python script.
import darklyrics
from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(get_all_lyrics("Slayer"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
