import requests
from bs4 import BeautifulSoup

def scrape_article_headline(article_link):
    # Send a GET request to the article link
    response = requests.get(article_link)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the headline element
    headline_element = soup.find('h1')
    print(soup.find_all('h1'))

    # Extract the headline text
    headline = headline_element.text.strip() if headline_element else "Headline not found"

    return headline

# Input the article link
article_link = "https://www.bleepingcomputer.com/news/security/germany-warns-of-17k-vulnerable-microsoft-exchange-servers-exposed-online/#google_vignette"

# Scrape the headline
headline = scrape_article_headline(article_link)

# Print the headline
print("Headline:", headline)
