from src.infra import SwapiApiConsumer
from .starships_list_colector import StarshipsListColector


def test_list():
    api_consumer = SwapiApiConsumer()
    starships_list_colector = StarshipsListColector(api_consumer)
    
    page = 1
    starships_list_colector.list(page)
    