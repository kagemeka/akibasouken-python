import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Genre():
  name: str 
  genre_id: str



def _scrape_genre(
  soup: bs4.BeautifulSoup,
) -> typing.List[Genre]:
  def find_elements() -> typing.NoReturn:
    return soup.find(class_='info_main').find_all(
      'dd',
    )[3].find_all('a')

  def extract_genre(elm: bs4.element.Tag) -> Genre:
    id_ = elm.get('href').split('/')[-2]
    return Genre(elm.text, id_)
  
  return [extract_genre(elm) for elm in find_elements()]



# class ScrapeGenre():

#   def __call__(
#     self,
#     soup: bs4.BeautifulSoup,
#   ) -> typing.List[Genre]:
#     self.__soup = soup
#     self.__scrape()
#     return self.__genres
  

#   def __find_elms(
#     self,
#   ) -> typing.NoReturn:
#     elms = self.__soup.find(
#       class_='info_main',
#     ).find_all(
#       'dd',
#     )[3].find_all(
#       'a',
#     )
#     self.__elms = elms


#   def __get_genre(
#     self,
#     elm: bs4.element.Tag,
#   ) -> Genre:
#     name = elm.text
#     id_ = elm.get(
#       'href',
#     ).split('/')[-2]
#     return Genre(name, id_)


  # def __scrape(
  #   self,
  # ) -> typing.NoReturn:
  #   self.__find_elms()
  #   self.__genres = [
  #     self.__get_genre(elm)
  #     for elm in self.__elms
  #   ]