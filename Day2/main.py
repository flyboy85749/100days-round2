import requests
from bs4 import BeautifulSoup

URL = "https://somesite.com"

response = requests.get(URL)
# print(response.text)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h1", class_="list-item__title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    count = 0
    for movie in movies:
        count += 1
        file.write(f"{count}) {movie}\n")
