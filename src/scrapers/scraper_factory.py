from typing import Union
import aiohttp
from bs4 import BeautifulSoup
from src.scrapers.staticscraper import StaticScraper
from src.scrapers.dynamicscrapper import DynamicScraper


class ScraperFactory:
    """
    A factory class for creating scraper instances.

    This class implements the factory design pattern to create either
    a StaticScraper or DynamicScraper instance, depending on the type of
    the website (static or dynamic). The decision is made based on the
    count of hyperlinks and presence of script tags in the web page.

    Use the create_scraper static method with a URL to get an appropriate
    scraper instance.
    """
    @staticmethod
    async def _is_static_site(url: str) -> bool:
        async with aiohttp.ClientSession() as session:
            scraper = StaticScraper(url)
            hrefs = await scraper.extract_links(session, url)

            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                scripts = soup.find_all('script')

                if scripts and len(hrefs) <= 2:
                    return False
        return True

    @staticmethod
    async def create_scraper(url: str) -> Union[StaticScraper, DynamicScraper]:

        if await ScraperFactory._is_static_site(url):
            return StaticScraper(url)
        else:
            return DynamicScraper(url)
