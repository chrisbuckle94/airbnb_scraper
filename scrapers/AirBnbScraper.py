from typing import Optional

import requests

from data.PropertyData import PropertyData
from scrapers.AbstractScraper import AbstractScraper

LISTING_IDS = ["33571268", "33090114", "50633275"]

TEMPLATE = "https://api.airbnb.com/v2/pdp_listing_details/{}?_format=for_native&key=d306zoyjsyarp7ifhu67rjxn52tv0t20"


class AirBnbScraper(AbstractScraper):

    @staticmethod
    def _get_property_data(listing_id: str, response_json: any) -> Optional[PropertyData]:
        if response_json is None:
            return None

        listing_detail = response_json.get("pdp_listing_detail")
        if listing_detail is None:
            return None

        title = listing_detail.get("p3_summary_title")
        property_type = listing_detail.get("room_and_property_type")
        bedroom = listing_detail.get("bedroom_label")
        bathroom = listing_detail.get("bathroom_label")

        amenities = [x.get("name") for x in listing_detail.get("listing_amenities") if x.get("name") is not None]

        return PropertyData(property_id=listing_id, property_name=title, property_type=property_type,
                            num_bedrooms=bedroom, num_bathrooms=bathroom, amenities_list=amenities)

    def scrape(self) -> [PropertyData]:
        data_list = []

        for listing_id in LISTING_IDS:
            request_url = TEMPLATE.format(listing_id)
            response = requests.get(request_url)
            if response.status_code != 200:
                continue

            data_list.append(self._get_property_data(listing_id, response.json()))

        return data_list
