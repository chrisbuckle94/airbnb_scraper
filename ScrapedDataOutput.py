from PropertyData import PropertyData


class ScrapedDataOutput:

    @staticmethod
    def print_property_data_json(data: dict[str, [PropertyData]]) -> None:
        print("---------------")
        for (data_source, property_data) in data.items():
            print(data_source)
            for property_data_item in property_data:
                print(property_data_item.json())
        print("---------------")
