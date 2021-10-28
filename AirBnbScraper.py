import requests

from AbstractScraper import AbstractScraper
from PropertyData import PropertyData

# TODO: Take links and parse out the listing ID?
# TODO: Read this from a JSON
LISTING_IDS = ["33571268", "33090114", "50633275"]

TEMPLATE = "https://api.airbnb.com/v2/pdp_listing_details/{}?_format=for_native&key=d306zoyjsyarp7ifhu67rjxn52tv0t20"


class AirBnbScraper(AbstractScraper):

    def scrape(self) -> [PropertyData]:
        data_list = []

        for listing_id in LISTING_IDS:
            # Make the request
            request_url = TEMPLATE.format(listing_id)

            response = requests.get(request_url)
            if response.status_code != 200:
                continue

            # Parse the JSON
            content = response.json()

            title = content["pdp_listing_detail"]["p3_summary_title"]
            property_type = content["pdp_listing_detail"]["room_and_property_type"]
            bedroom = content["pdp_listing_detail"]["bedroom_label"]
            bathroom = content["pdp_listing_detail"]["bathroom_label"]

            amenities = []
            amenities_raw = content["pdp_listing_detail"]["listing_amenities"]
            for amenity in amenities_raw:
                amenities.append(amenity["name"])

            data_list.append(
                PropertyData(property_id=listing_id, property_name=title, property_type=property_type,
                             num_bedrooms=bedroom, num_bathrooms=bathroom, amenities_list=amenities))

        return data_list
