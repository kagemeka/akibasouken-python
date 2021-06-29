import bs4 
import dataclasses
import re
import typing



@dataclasses.dataclass 
class Metadata():
  title: str 
  media: str
  year: int
  season: int
  official_site: str = None
  


class ScrapeMetadata():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Metadata:
    self.__soup = soup 
    self.__scrape()
    return self.__meta

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_title_media()
    self.__get_year_season()
    self.__get_official_site()
    self.__meta = Metadata(
      self.__title,
      self.__media,
      self.__year,
      self.__season,
      self.__official_site,
    )
  

  def __get_title_media(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      class_='itemTitle',
    )
    title = section.find(
      'h1',
    ).text
    media = section.find(
      class_='category',
    ).text
    self.__title = title
    self.__media = media


  def __get_year_season(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      class_='info_main',
    )
    url = section.find(
      'dd',
    ).find('a').get('href')
    ptn = re.compile(
      r'^.*\?season=(\d+)'
      r'&year=(\d+)$',
    )
    m = re.match(ptn, url)
    self.__year = m.group(2)
    self.__season = m.group(1)
  

  def __get_official_site(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='specBox',
    ).find('a')
    url = (
      elm.get('href') if elm
      else None 
    )
    self.__official_site = url