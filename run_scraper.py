from typing import Dict, List

from data.PropertyData import PropertyData
from scrapers.AirBnbScraper import AirBnbScraper
from utils.ScrapedDataOutput import ScrapedDataOutput

SCRAPERS = {"AIRBNB": AirBnbScraper()}


def _run_scrapers() -> Dict[str, List[PropertyData]]:
    all_scraped_data = {}

    for (name, scraper) in SCRAPERS.items():
        all_scraped_data[name] = scraper.scrape()

    return all_scraped_data


if __name__ == "__main__":
    data = _run_scrapers()
    ScrapedDataOutput.print_json(data)
