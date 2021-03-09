import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

flashback = input("What year would you like to return to? Type the date in this format YYYY-MM-DD: \n")

URL = "https://www.billboard.com/charts/hot-100/" + flashback

response = requests.get(URL)
# print(response.text)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song")

song_titles = [song.getText() for song in all_songs]
songs = song_titles[::-1]
print(songs)
# with open("movies.txt", mode="w") as file:
#     count = 0
#     for movie in movies:
#         count += 1
#         file.write(f"{count}) {movie}\n")
