from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
hundred_films = response.text

soup = BeautifulSoup(hundred_films, "html.parser")

source = soup.find_all(name="h3", class_="title")
films = []
for film in source:
    new_item = film.text + "\n"
    films.append(new_item)
films.reverse()
with open("films.txt", "a") as file:
    for film in films:
        file.write(film)
