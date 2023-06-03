import asyncio
from src.scrapers.staticscraper import StaticScraper
from src.scrapers.dynamicscrapper import DynamicScraper
from src.sitmap_creator import create


# def main(url):
#     url = normalize_url(url)
#     is_url_exists(url)

#     return url


if __name__ == "__main__":
    scraper = DynamicScraper('https://dzen.ru/')
    asyncio.run(create(scraper.crawl(), scraper.domain))
