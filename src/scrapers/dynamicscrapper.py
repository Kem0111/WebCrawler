from typing import List
from pyppeteer import launch, browser
from pyppeteer.errors import NetworkError, TimeoutError
from src.scrapers.abstract_scraper import Scraper


class DynamicScraper(Scraper):
    """
    DynamicScraper is a class for scraping dynamic websites
    using a headless browser.
    """

    async def extract_links(self, browser: browser.Browser,
                            url: str) -> List[str]:

        page = await browser.newPage()
        try:
            await page.goto(url, waitUntil='networkidle0')
            hrefs = await page.evaluate('''() => {
                    return Array.from(
                        document.querySelectorAll('a')
                    ).map(a => a.href);
                }''')
            return hrefs
        except (NetworkError, TimeoutError):
            return []
        except Exception:
            return []
        finally:
            await page.close()

    async def crawl(self):

        browser = await launch()

        try:
            async for link in self._process_links(browser):
                yield link
        finally:
            await browser.close()
