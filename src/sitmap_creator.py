import xml.etree.ElementTree as ET
from xml.dom import minidom


async def create(crawl, domain):
    urlset = ET.Element("urlset", xmlns=domain)
    async for url in crawl:
        url_element = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_element, "loc")
        loc.text = url

    xml_string = ET.tostring(urlset, 'utf-8')
    parsed_string = minidom.parseString(xml_string)
    pretty_string = parsed_string.toprettyxml(indent="   ")

    with open(f"sitemaps/{domain}_sitemap.xml", "w") as f:
        f.write(pretty_string)
