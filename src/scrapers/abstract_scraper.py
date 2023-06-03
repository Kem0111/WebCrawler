from abc import ABC, abstractmethod
import asyncio
from collections import deque
from ctypes import Union
from itertools import chain
from typing import AsyncGenerator, List
from urllib.parse import urlparse

from aiohttp import ClientSession
from pyparsing import Any
from pyppeteer import browser


class Scraper(ABC):
    MAX_DEEP = 2

    def __init__(self, start_url: str) -> None:
        self.start_url = start_url
        self.domain = urlparse(start_url).netloc
        self.queue = deque([start_url])
        self.visited = set([start_url])

    @abstractmethod
    async def extract_links(self, session, url):
        pass

    async def _fill_queue(self, links: List[str]) -> None:
        for link in links:
            if link not in self.visited and\
               self.domain == urlparse(link).netloc:

                self.visited.add(link)
                self.queue.append(link)

    async def _process_links(self, session:
                             Union[ClientSession, browser.Browser]
                             ) -> AsyncGenerator[str, None]:
        """
        Process all URLs in the queue, extracting links from each
        webpage and  adding them to the queue. This is done up to MAX_DEEP
        times to avoid infinite recursion.
        """
        current_deep = 0

        while current_deep < self.MAX_DEEP:
            tasks = []

            while self.queue:
                current_url = self.queue.popleft()
                tasks.append(self.extract_links(session, current_url))
                yield current_url

            result: List[Any] = await asyncio.gather(*tasks)
            links: List[str] = list(chain.from_iterable(result))

            await self._fill_queue(links)

            current_deep += 1

        # gives the remaining links in the queue
        for _ in range(len(self.queue)):
            yield self.queue.popleft()

    @abstractmethod
    async def crawl(self):
        """
        Begin the web scraping process.

        This method should be implemented in subclasses to handle the
        specifics of the web scraping process for different types of webpages.
        """
        pass
