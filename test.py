import requests

# TODO: Take links and parse out the listing ID
LISTING_IDS = ["33571268", "33090114", "50633275"]

EXAMPLE = "https://api.airbnb.com/v2/pdp_listing_details/33090114?_format=for_native&key=d306zoyjsyarp7ifhu67rjxn52tv0t20"
TEMPLATE = "https://api.airbnb.com/v2/pdp_listing_details/{}?_format=for_native&key=d306zoyjsyarp7ifhu67rjxn52tv0t20"

if __name__ == "__main__":
    for listing_id in LISTING_IDS:
        # Make the request
        request_url = TEMPLATE.format(listing_id)
        print(request_url)
        x = requests.get(request_url)
        print(x.status_code)
        if x.status_code != 200:
            continue

        # Parse the JSON
        content = x.json()

        print("---------------------------")
        print(listing_id)

        # Output the useful data
        title = content["pdp_listing_detail"]["p3_summary_title"]
        print(title)

        property_type = content["pdp_listing_detail"]["room_and_property_type"]
        print(property_type)

        bedroom = content["pdp_listing_detail"]["bedroom_label"]
        print(bedroom)

        bathroom = content["pdp_listing_detail"]["bathroom_label"]
        print(bathroom)

        amenities = content["pdp_listing_detail"]["listing_amenities"]
        for amenity in amenities:
            print(amenity["name"])

        print("---------------------------")
