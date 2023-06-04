[![Pytest(+ Linter)](https://github.com/Kem0111/WebCrawler/actions/workflows/webcrawler.yml/badge.svg)](https://github.com/Kem0111/WebCrawler/actions/workflows/webcrawler.yml) <a href="https://codeclimate.com/github/Kem0111/WebCrawler/maintainability"><img src="https://api.codeclimate.com/v1/badges/73f701f36e2eb380c7bb/maintainability" /></a> <a href="https://codeclimate.com/github/Kem0111/WebCrawler/test_coverage"><img src="https://api.codeclimate.com/v1/badges/73f701f36e2eb380c7bb/test_coverage" /></a>



# My WebCrawler

This repository houses a unique web crawler with two types of parsers: StaticParser and DynamicParser. It also includes a factory that determines which parser to use based on the type of website being crawled.

---
## Features

1. StaticParser: This parser is used when a site returns static HTML. It is incredibly fast, able to process over 1000 requests in less than 3 seconds.
2. DynamicParser: This parser is utilized for dynamic websites that make use of JavaScript, where the links are not directly present in the HTML. It simulates a browser to ensure that all links are parsed, even if they are generated dynamically. This parser operates slower than the StaticParser but guarantees successful link parsing, given the IP is not banned.
3. Parser Factory: The factory determines which parser to use based on the type of website. Static websites trigger the StaticParser, and dynamic websites with JS trigger the DynamicParser.
Sitemap Generation: After the parsing process, a .xml file is generated in the sitemaps directory, which represents the site's sitemap.
4. Database Storage: The parsed data is stored in a database for later use. If necessary, a results.csv file can be generated, which provides information in the format: URL, Processing Time, Links Count, Path.

---

## ⚠️ Warning

Please note that these parsers do not respect robots.txt and do not operate through proxies. As a result, websites may ban your IP address due to a high number of requests per second. Use responsibly and consider the ethical implications before performing large-scale web scraping.