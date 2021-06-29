import bs4 
import dataclasses
import re
import typing



@dataclasses.dataclass 
class Studio():
  name: str
  studio_id: int = None



class ScrapeStudio():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Studio:
    self.__soup = soup
    self.__scrape()
    return self.__studio


  def __find_elm(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='info_main',
    ).find_all('dd')[2].find(
      'a',
    )
    self.__elm = elm


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elm()
    elm = self.__elm
    if elm is None:
      self.__studio = Studio(
        None,
        None,
      )
      return
    studio = elm.text
    url = elm.get('href')
    ptn = re.compile(
      r'^.*\?studio=(\d+).*$',
    )
    m = re.match(ptn, url)
    studio_id = int(m.group(1))
    self.__studio = Studio(
      studio,
      studio_id,
    )