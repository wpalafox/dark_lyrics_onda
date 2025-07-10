DarkLyrics Scraper
This Python script scrapes metal band song lyrics from DarkLyrics.com using Selenium and the darklyrics Python module. It compiles the lyrics into a structured Excel file for further analysis or collection.

Features
Automatically navigates DarkLyrics using Selenium WebDriver.

Scrapes band names (starting with 'A' by default).

Retrieves all songs and corresponding lyrics using darklyrics API.

Saves the data into an Excel file with columns: BAND, SONG, LYRICS.

Skips entries with missing lyrics and logs them.

Requirements
Python 3.6+

Google Chrome installed

ChromeDriver (matching your Chrome version)

Installation
Clone this repository or download the script.

Install required packages:

bash
Copy
Edit
pip install selenium beautifulsoup4 pandas darklyrics
Download ChromeDriver and place it in the same directory as the script.

Ensure your ChromeDriver version matches your installed Chrome version.

Usage
Run the script:

bash
Copy
Edit
python your_script_name.py
This will:

Launch a Chrome browser instance.

Navigate to the DarkLyrics website.

Click on the "A" section (bands starting with A).

Extract all listed bands under "A", get their songs and lyrics.

Save the results to test_a.xlsx.

Notes
Currently, only bands starting with the letter 'A' are scraped. To extend this, modify the alpha list in the script:

python
Copy
Edit
alpha = list("abcdefghijklmnopqrstuvwxyz")
Introduces random sleep delays (2–5 seconds) between requests to avoid hammering the server.

Error handling is included for missing songs or lyrics.

Disclaimer
This script is for educational and research purposes only. Respect the website's terms of service when scraping data.
