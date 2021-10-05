from .yearly_anime import YearlyAnime, scrape_yearly_anime
import bs4 
import requests
import typing
import datetime



def scrape_current_animes() -> typing.Iterator[YearlyAnime]:
  SEASON = ('winter', 'spring', 'summer', 'autumn')
  BASE_URL = 'https://akiba-souken.com/anime/'

  def _calc_seasons() -> typing.Tuple[str, str]:
    dt = datetime.datetime.now()
    i = dt.month // 3 % 4
    return (SEASON[i], SEASON[(i - 1) % 4])
  
  def compute_urls() -> typing.Iterator[str]:
    return (f'{BASE_URL}{s}' for s in _calc_seasons())
  
  def make_soup(url: str) -> bs4.BeautifulSoup:
    response = requests.get(url)
    return bs4.BeautifulSoup(response.content, 'html.parser')
  
  for url in compute_urls():
    print(url)
    soup = make_soup(url)
    section = soup.find(id='contents')
    animes = section.find_all(class_='itemBox')
    for anime in animes: yield scrape_yearly_anime(anime)



# class ScrapeComingAnimes():

#   __SEASON = (
#     'winter',
#     'spring',
#     'summer',
#     'autumn',
#   )


#   def __call__(
#     self,
#   ) -> typing.Iterator[
#     YearlyAnime
#   ]:
#     self.__make_soup()
#     return self.__scrape()    


#   def __calc_season(
#     self,
#   ) -> typing.NoReturn:
#     dt = datetime.now()
#     i = dt.month // 3 % 4
#     season = self.__SEASON[i]
#     print(season)
#     self.__season = season
  

#   def __init__(
#     self,
#   ) -> typing.NoReturn:
#     base_url = (
#       'https://'
#       'akiba-souken.com/'
#       'anime/'
#     )
#     self.__calc_season()
#     season = self.__season
#     self.__url = (
#       f'{base_url}{season}'
#     )
  

#   def __make_soup(
#     self,
#   ) -> typing.NoReturn:
#     response = requests.get(
#       self.__url,
#     )
#     soup = bs4.BeautifulSoup(
#       response.content,
#       'html.parser',
#     )
#     self.__soup = soup

  
#   def __scrape(
#     self,
#   ) -> typing.Iterator[
#     YearlyAnime
#   ]:
#     section = self.__soup.find(
#       id='contents',
#     )
#     animes = section.find_all(
#       class_='itemBox',
#     )
#     get = ScrapeYearlyAnime()
#     for anime in animes:
#       yield get(anime)