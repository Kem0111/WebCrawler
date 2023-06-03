from urllib.parse import urljoin
import aiohttp
from bs4 import BeautifulSoup
from src.scrapers.abstract_scraper import Scraper


class StaticScraper(Scraper):

    async def extract_links(self, session, url):
        try:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                return [
                    urljoin(url, link.get('href'))
                    for link in soup.find_all('a', href=True)
                ]
        except Exception:
            return []

    async def crawl(self):

        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=2)
        ) as session:

            async for link in self._process_links(session):
                yield link
