import requests


def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException:
        return False
