from AirBnbScraper import AirBnbScraper
from PropertyData import PropertyData
from ScrapedDataOutput import ScrapedDataOutput

SCRAPERS = {"AIRBNB": AirBnbScraper()}


def _run_scrapers() -> dict[str, [PropertyData]]:
    all_scraped_data = {}

    for (name, scraper) in SCRAPERS.items():
        all_scraped_data[name] = scraper.scrape()

    return all_scraped_data


if __name__ == "__main__":
    data = _run_scrapers()
    ScrapedDataOutput.print_property_data_json(data)
