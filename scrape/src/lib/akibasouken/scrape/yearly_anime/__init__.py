import bs4 
import dataclasses
import typing
from .twitter import Twitter, _scrape_twitter
from .broadcast import Broadcast, _scrape_broadcast
from ..anime import Anime, scrape_anime



@dataclasses.dataclass
class YearlyAnime(Anime):
  twitter: Twitter
  boardcasts: typing.List[Broadcast]


def scrape_yearly_anime(
  section: bs4.element.Tag,
) -> YearlyAnime:
  def get_anime_id() -> int:
    url = section.find(class_='mTitle').find('a').get('href')
    return int(url.split('/')[-2])
  
  anime = scrape_anime(get_anime_id())
  return YearlyAnime(
    anime.anime_id,
    anime.staffs,
    anime.voice_actors,
    anime.score,
    anime.metadata,
    anime.studios,
    anime.genres,
    anime.long_text,
    anime.tags,
    _scrape_twitter(section),
    _scrape_broadcast(section),
  )  




# class ScrapeYearlyAnime():

#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> YearlyAnime:
#     self.__section = section
#     self.__scrape()
#     return self.__anime
  

#   def __get_anime_id(
#     self,
#   ) -> typing.NoReturn:
#     url = self.__section.find(
#       class_='mTitle',
#     ).find('a').get('href')
#     id_ = url.split('/')[-2]
#     self.__id = int(id_)


#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     self.__get_anime_id()
#     anime =  ScrapeAnime()(
#       self.__id,
#     )
#     scrapes = (
#       ScrapeTwitter(),
#       ScrapeBroadcast(),
#     )
#     res = (
#       scrape(self.__section)
#       for scrape in scrapes
#     )
#     self.__anime = YearlyAnime(
#       anime.anime_id,
#       anime.staffs,
#       anime.voice_actors,
#       anime.score,
#       anime.metadata,
#       anime.studios,
#       anime.genres,
#       anime.long_text,
#       anime.tags,
#       *res,
#     )