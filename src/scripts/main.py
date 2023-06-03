#!/usr/bin/env python3
import asyncio
import time
from src.scrapers.scraper_factory import ScraperFactory
from src.sitmap_creator import create_sitemap
from src.db.db_interaction import handle_database_interaction
from src.db.querys import CREATE_TABLE, ADD_RESULT
from src.utils.url_pars import normalize_url
from src.utils.validate import check_error


async def main():
    url = input('Enter website: ').strip()
    url = normalize_url(url)
    check_error(url)

    start_time = time.time()
    scraper = await ScraperFactory.create_scraper(url)
    await create_sitemap(scraper.crawl(), scraper.domain)
    res_time = time.time() - start_time

    table_data = (
        scraper.domain,
        float(f"{res_time:.2f}"),
        len(scraper.visited),
        f"sitemaps/{scraper.domain}_sitemap.xml"
    )

    handle_database_interaction(CREATE_TABLE)
    handle_database_interaction(ADD_RESULT, table_data)


if __name__ == "__main__":
    asyncio.run(main())
