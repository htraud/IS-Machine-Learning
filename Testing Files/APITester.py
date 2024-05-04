import requests

api_key = 'c21e26ec2ea54eb89d1c64536f904da0'  # Replace 'YOUR_API_KEY' with your actual News API key
url = 'https://newsapi.org/v2/everything?q=apple&from=2024-03-30&to=2024-03-30&sortBy=popularity&apiKey=c21e26ec2ea54eb89d1c64536f904da0'

try:
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    for article in articles:
        title = article['title']
        source = article['source']['name']
        print(f"{title} - {source}")
except requests.RequestException as e:
    print("Error fetching news:", e)
