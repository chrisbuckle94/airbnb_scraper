from abc import ABC, abstractmethod

from data.PropertyData import PropertyData


class AbstractScraper(ABC):

    @abstractmethod
    def scrape(self) -> [PropertyData]:
        pass
