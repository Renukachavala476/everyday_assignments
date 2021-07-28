import json
import requests
data=requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-06-27&sortBy=publishedAt&apiKey=f17be65505324f969e22a9cd36ed125b")
extracteddata=data.json()
print(extracteddata)