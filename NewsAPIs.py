import requests
import json

# NYT API initialization
NYT_API_KEY = 'D4275sWVK1aZN5pKa5c58oH2O5UxhLl3'
NYT_API_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

params = {
    'api-key': NYT_API_KEY,
    'begin_date': '20230101',  # YYYYMMDD format
    'end_date': '20231231',    # YYYYMMDD format
    'offset': 0,

}

# Gather data from NYT API and format into json file
nytresponse = requests.get(NYT_API_URL, params=params)
nytdata = nytresponse.json()

# Dump json data from nyt into own file in case of review
with open('nytdata.json', 'w') as file:
        json.dump(nytdata, file, indent=4)
    

# Process the response data from NYT
with open('Headlines_and_Dates.txt', 'w') as file:
    for article in nytdata['response']['docs']:
        nytheadlines=article['headline']['main'] + ' - NYT'
        nyt_published_date = article['pub_date']
        file.write(f"{nyt_published_date}: {nytheadlines}\n")


# GUARDIAN API initialization
GUARDIAN_API_KEY = '8c61836e-a824-40e3-a287-d37b1d688b03'
GUARDIAN_API_URL = f'https://content.guardianapis.com/search?&api-key={GUARDIAN_API_KEY}&section=news'

params = {
    'from-date': '2023-01-01',
    'to-date': '2023-12-31',
    'show-fields': 'headline,webPublicationDate,keyword',
    'order-by': 'relevance',
    'page-size': 78  # Number of results per page
    
}

# Gather data from Guardian API and format into json file
guardianresponse = requests.get(GUARDIAN_API_URL, params=params)
guardiandata = guardianresponse.json()

# Dump json data from nyt into own file in case of review
with open('guardiandata.json', 'w') as file:
        json.dump(guardiandata, file, indent=4)

# Process response data from GUARDIAN API
with open('Headlines_and_Dates.txt', 'a') as file:
    for article in guardiandata['response']['results']:
        if article['fields']['headline'] != 'Corrections and clarifications' and article['fields']['headline'] != 'For the record' and article['fields']['headline'] != 'From the archive':
            guardianheadlines = article['fields']['headline'] + ' - Guardian'
            guardian_publication_date = article['webPublicationDate']
            file.write(f"{guardian_publication_date}: {guardianheadlines}\n")
