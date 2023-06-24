from bs4 import BeautifulSoup
import requests


def repeat():
    response = requests.get(url="https://news.ycombinator.com/news")
    yc_webp = response.text

    soup = BeautifulSoup(yc_webp, 'html.parser')
    # print(soup.title)

    articles = soup.find_all(name="span", class_="titleline")

    # list comprehension used
    upvotes = [int(score.getText().split()[0])
               for score in soup.find_all(name="span", class_="score")]

    article_text = []
    article_links = []

    for article in articles:
        article_text.append(article.getText())
        anchortag = article.select_one("span a")
        article_links.append(anchortag.get("href"))

    # print(article_text)
    # print(article_links)
    # print(upvotes)

    max_ind = upvotes.index(max(upvotes))
    print(
        f"{article_text[max_ind]},\n{article_links[max_ind]},\n{upvotes[max_ind]}")

while(True):
    repeat()