import bs4 
import dataclasses
import re
import typing



@dataclasses.dataclass 
class Studio():
  name: str
  studio_id: int = None



def _scrape_studio(
  soup: bs4.BeautifulSoup,
) -> typing.List[Studio]:
  def find_elements() -> typing.List[bs4.element.Tag]:
    return soup.find(class_='info_main').find_all(
      'dd',
    )[2].find_all('a')

  def extract_studio(elm: bs4.element.Tag) -> Studio:
    studio = elm.text
    url = elm.get('href')
    ptn = re.compile(r'^.*\?studio=(\d+).*$')
    m = re.match(ptn, url)
    studio_id = int(m.group(1))
    return Studio(studio, studio_id)

  return [extract_studio(e) for e in find_elements()]
