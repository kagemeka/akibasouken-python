
import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Tag():
  name: str


def _scrape_tag(soup: bs4.BeautifulSoup) -> typing.List[Tag]:
  elements = soup.find(class_='tag').find_all('a')[:-1]
  return [Tag(e.text) for e in elements]

