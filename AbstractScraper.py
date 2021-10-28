from abc import ABC, abstractmethod

from PropertyData import PropertyData


class AbstractScraper(ABC):

    @abstractmethod
    def scrape(self) -> [PropertyData]:
        pass
