import asyncio
from src.scrapers.scraper_factory import ScraperFactory
# from src.scrapers.staticscraper import StaticScraper
# from src.scrapers.dynamicscrapper import DynamicScraper
from src.sitmap_creator import create_sitemap


# def main(url):
#     url = normalize_url(url)
#     is_url_exists(url)

#     return url


async def main():
    url = 'https://vk.com'
    scraper = await ScraperFactory.create_scraper(url)
    await create_sitemap(scraper.crawl(), scraper.domain)

if __name__ == "__main__":
    asyncio.run(main())
