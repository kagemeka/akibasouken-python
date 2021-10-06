import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Twitter():
  username: typing.Optional[str] = None


def _scrape_twitter(section: bs4.element.Tag) -> Twitter:
  def get_url() -> typing.Optional[str]:
    elm = section.find(class_='officialTwitter')
    return elm.get('href') if elm else None
  
  def get_username(url: str) -> typing.Optional[str]:
    return url.split('/')[-1]
  
  url = get_url()
  username = None if url is None else get_username(url)
  return Twitter(username)
