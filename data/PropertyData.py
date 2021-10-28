import json


class PropertyData:

    def __init__(self, property_id, property_name, property_type, num_bedrooms, num_bathrooms, amenities_list):
        self.property_id = property_id
        self.property_name = property_name
        self.property_type = property_type
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.amenities = amenities_list

    def json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
