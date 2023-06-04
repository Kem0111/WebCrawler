import pytest
from unittest.mock import patch, MagicMock
from urllib.error import URLError
from src.utils.validate import check_error
from src.utils.exeptions import UrlNotAccessible


def test_check_error_when_url_is_accessible():
    with patch("urllib.request.urlopen", return_value=MagicMock()):
        assert check_error("http://example.com") is True


def test_check_error_when_url_is_not_accessible():
    with patch("urllib.request.urlopen", side_effect=URLError):
        with pytest.raises(UrlNotAccessible) as excinfo:
            check_error("http://exampl")
        assert isinstance(excinfo.value, UrlNotAccessible)
