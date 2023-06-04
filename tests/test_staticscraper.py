import aiohttp
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.scrapers.staticscraper import StaticScraper
from aiohttp import ClientSession


@pytest.mark.asyncio
async def test_extract_links():
    test_html = (
        '<a href="http://test.com/test1">Test '
        '1</a><a href="/test2">Test 2</a>'
    )
    scraper = StaticScraper("http://test.com")

    mock_response = AsyncMock()
    mock_response.text = AsyncMock(return_value=test_html)

    mock_session = MagicMock()
    mock_session.get.return_value.__aenter__ = AsyncMock(
        return_value=mock_response
    )

    links = await scraper.extract_links(mock_session, "http://test.com")

    assert links == ["http://test.com/test1", "http://test.com/test2"]


class AsyncIteratorWrapper:
    def __init__(self, items):
        self.items = items

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.items:
            raise StopAsyncIteration
        return self.items.pop(0)


@pytest.mark.asyncio
@patch.object(ClientSession, 'get')
@patch.object(StaticScraper, '_process_links')
async def test_crawl(mock_process_links, mock_get):

    mock_process_links.return_value = AsyncIteratorWrapper([
            "http://test.com/test1",
            "http://test.com/test2"
        ]
    )

    scraper = StaticScraper("http://test.com")

    results = []
    async for link in scraper.crawl():
        results.append(link)

    assert results == ["http://test.com/test1", "http://test.com/test2"]

    # Assert that _process_links was called with the correct arguments
    mock_process_links.assert_called_once()
    assert isinstance(mock_process_links.call_args[0][0],
                      aiohttp.ClientSession)

    # Assert that the get method was not called
    mock_get.assert_not_called()
