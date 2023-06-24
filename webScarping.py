import requests
from bs4 import BeautifulSoup
import csv

# opening a csv to store data after scraping
csv_file = open('scraped_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'Summary', 'Video'])


# Making a soup of the website that is to be scraped 
response = requests.get(url='http://coreyms.com')
my_site = response.text
soup = BeautifulSoup(my_site, 'lxml')


articleheads = [article.text for article in soup.find_all(
    name="a", class_="entry-title-link")]
descriptions = [article.text.strip()
                for article in soup.find_all(name="div", class_="entry-content")]

# short_link = pyshorteners.Shortener()
# short_link.tinyurl.short()
links = []
for link in soup.find_all(name="iframe", class_="youtube-player"):
    try:
        # Extracts Video ID from Embed URL
        vid_id = link.get('src').split('/')[4].split('?')[0]
        links.append(f"https://www.youtube.com/watch?v={vid_id}")
    except Exception as e:
        vid_id = None

for i in range(0, len(links)):
    print(articleheads[i])
    print(descriptions[i])
    print(links[i])
    print("\n")
    csv_writer.writerow([articleheads[i], descriptions[i], links[i]])

# Scraping Part Completed

csv_file.close()

print("Done Scraping")
