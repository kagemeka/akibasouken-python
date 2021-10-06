import bs4 
import dataclasses
import requests
import typing
from .staff import Staff, _scrape_staff
from .voice_actor import VoiceActor, _scrape_voice_actor
from .score import Score, _scrape_score
from .metadata import Metadata, _scrape_metadata
from .studio import Studio, _scrape_studio
from .genre import Genre, _scrape_genre
from .long_text import LongText, _scrape_long_text
from .tag import Tag, _scrape_tag



@dataclasses.dataclass
class Anime():
  anime_id: int
  staffs: typing.List[Staff]
  voice_actors: typing.List[VoiceActor]
  score: Score
  metadata: Metadata
  studios: typing.List[Studio]
  genres: typing.List[Genre]
  long_text: LongText
  tags: typing.List[Tag]



def scrape_anime(anime_id: int) -> Anime:
  BASE_URL = 'https://akiba-souken.com/anime/'
  response = requests.get(f'{BASE_URL}{anime_id}')
  soup = bs4.BeautifulSoup(response.content, 'html.parser')
  return Anime(
    anime_id,
    _scrape_staff(soup),
    _scrape_voice_actor(soup),
    _scrape_score(soup),
    _scrape_metadata(soup),
    _scrape_studio(soup),
    _scrape_genre(soup),
    _scrape_long_text(soup),
    _scrape_tag(soup),
  )