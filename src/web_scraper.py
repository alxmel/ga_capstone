""" This script is responsbile for scraping the raw data that will be used in my model """
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Headers for user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# HTTP GET request to Wiki page
r = requests.get("https://en.wikipedia.org/wiki/List_of_immigration_raids_and_arrests_in_the_second_Trump_presidency", headers=headers)

# Save the contents using BeautifulSoup
soup = BeautifulSoup(r.content, 'lxml')

# The Wiki page doesn't follow a traditional DOM tree, so grabbing everything at once
# years = soup.find_all("h2")
months = soup.find_all("h3")
paragraphs = soup.find_all("p")

# Storing the months and actual text into their own arrays
months_array = []
paragraphs_array = []

# Populating the respective arrays
for month in months:
    months_array.append(month.text)

for p in paragraphs:
    paragraphs_array.append(p.text)

# Creating the columns for the DataFrame, then will begin appending each web-scraped year and paragraph
df = pd.DataFrame(columns=["month", "event"])

# Looping through each paragraph, checking which month is mentioned, and appending to the DataFrame the Month and Paragraph
for i in paragraphs_array:
    match i:
        case jan if "January".lower() in i.lower():
            new_row = {'month': "January", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case feb if "February".lower() in i.lower():
            new_row = {'month': "February", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case mar if "March".lower() in i.lower():
            new_row = {'month': "March", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case apr if "April".lower() in i.lower():
            new_row = {'month': "April", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case may if "May".lower() in i.lower():
            new_row = {'month': "May", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case jun if "June".lower() in i.lower():
            new_row = {'month': "June", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case jul if "July".lower() in i.lower():
            new_row = {'month': "July", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case aug if "August".lower() in i.lower():
            new_row = {'month': "August", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case sep if "September".lower() in i.lower():
            new_row = {'month': "September", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case oct if "October".lower() in i.lower():
            new_row = {'month': "October", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case nov if "November".lower() in i.lower():
            new_row = {'month': "November", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case dec if "December".lower() in i.lower():
            new_row = {'month': "December", "event": i}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        case _:
             print(f"Could not find month for entry, requires manual review: {i}")

# Save the DataFrame to CSV
df.to_csv("../data/raw/trackingice.csv", index=False)
