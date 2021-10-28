# airbnb_scraper

A project to scrape data from airbnb for a select few listings.

It currently only scrapes airbnb, but designed to make scraping new providers easier.

### Installing

* Install Python 3.6+
    * virtualenv recommended
* `pip install -r requirements.txt`

### Running

* `py run_scraper.py`

### Future work

* Potential improvements
    * airbnb scraper
        * Read listing URL/id's from a JSON file
        * Log errors on early exits/failures in scraper
    * Scrapers
        * Add another scraper
        * Read scrapers to use from a JSON file
    * Data output
        * Output to a JSON file
        * Output each scraper's data separately
        * Output to other formats than JSON
* Add tests for:
    * Parser (use fake JSON responses)
    * General data flow (use fake property data)
