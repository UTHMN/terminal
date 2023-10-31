import requests

url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"


while True:
    r = requests.get(url)
    rContent = r.content
    print(rContent)
    input()
