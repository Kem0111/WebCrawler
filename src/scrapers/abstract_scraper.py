from abc import ABC, abstractmethod
import asyncio
from collections import deque
from itertools import chain
from urllib.parse import urlparse


class Scraper(ABC):
    MAX_DEEP = 2

    def __init__(self, start_url) -> None:
        self.start_url = start_url
        self.domain = urlparse(start_url).netloc
        self.queue = deque([start_url])
        self.visited = set([start_url])

    @abstractmethod
    async def extract_links(self, session, url):
        pass

    async def _fill_queue(self, links):
        for link in links:
            if link not in self.visited and\
               self.domain == urlparse(link).netloc:

                self.visited.add(link)
                self.queue.append(link)

    async def _process_links(self, session):
        current_deep = 0

        while current_deep < self.MAX_DEEP:
            tasks = []

            while self.queue:
                current_url = self.queue.popleft()
                tasks.append(self.extract_links(session, current_url))
                yield current_url

            result = await asyncio.gather(*tasks, return_exceptions=True)
            links = list(chain.from_iterable(result))

            await self._fill_queue(links)

            current_deep += 1

        for _ in range(len(self.queue)):
            yield self.queue.popleft()

    @abstractmethod
    async def crawl(self):
        pass
