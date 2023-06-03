from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from exeptions import UrlNotAccessible


def is_url_exists(url):
    try:
        urlopen(Request(url))
        return True
    except (HTTPError, URLError) as e:
        raise UrlNotAccessible(f"Unable to access {url}. Reason: {str(e)}")
