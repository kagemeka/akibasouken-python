import bs4 
import dataclasses
import typing


@dataclasses.dataclass
class LongText():
  commentary: typing.Optional[str] = None
  overview: typing.Optional[str] = None


def _scrape_long_text(soup: bs4.BeautifulSoup) -> LongText:
  def get_commentary() -> typing.Optional[str]:
    elm = soup.find(class_='commentary')
    return elm.text if elm else None
  
  def get_overview() -> typing.Optional[str]:
    elm = soup.find(class_='storyLine')
    return elm.text if elm else None
      
  return LongText(get_commentary(), get_overview())


