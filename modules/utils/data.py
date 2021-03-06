from io import BytesIO
import requests
from requests.exceptions import RequestException


def prepare_binary_from_url(url):
    try:
        content = requests.get(url, timeout=(1, 3)).content
    except RequestException:
        pass
    else:
        return BytesIO(content)
