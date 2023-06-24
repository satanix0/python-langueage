from urllib import response
from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_wp = response.text

soup = BeautifulSoup(empire_wp, 'html.parser')
movies = soup.find_all(name="h3", class_="title")
movies_list = []
for i in movies:
    movies_list.append(i.getText())

# print(movies_list)
n = len(movies_list)
print(n)
with open('Projects\D45_MovieDB\movies.txt', 'w', encoding='utf-8') as fp:
    for i in range(n):
        fp.write(movies_list[n-i-1]+"\n")

print("doen")
