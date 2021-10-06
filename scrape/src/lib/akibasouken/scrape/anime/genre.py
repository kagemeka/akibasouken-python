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

