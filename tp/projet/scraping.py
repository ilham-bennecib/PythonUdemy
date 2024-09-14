import requests


def get_all_url():
    r = requests.get("https://genius.com/api/artists/29743/songs?page=1&sort=popularity")
    print(r.status_code)
    print(r.json())

get_all_url()