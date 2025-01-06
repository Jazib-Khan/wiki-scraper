import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.string)

# Get all the links
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linktoScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Food")
