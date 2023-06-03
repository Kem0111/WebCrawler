from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from src.utils.exeptions import UrlNotAccessible


def check_error(url):
    try:
        with urlopen(Request(url)):
            return True
    except (HTTPError, URLError) as e:
        raise UrlNotAccessible(f"Unable to access {url}. Reason: {str(e)}")
