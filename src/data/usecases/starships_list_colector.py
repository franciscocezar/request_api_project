from typing import List, Dict, Type
from src.domain.usecases import StarshipsListColectorInterface
from src.infra import SwapiApiConsumer

class StarshipsListColector(StarshipsListColectorInterface):
    '''StarshipListColector usecase'''

    def __init__(self, api_consumer: Type[SwapiApiConsumer]):
        self.__api_consumer = api_consumer

    def list(self, page) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        print(response)
