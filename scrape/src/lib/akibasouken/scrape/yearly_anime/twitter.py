import bs4 
import dataclasses
import typing
import re 


@dataclasses.dataclass
class Twitter():
  username: typing.Optional[str] = None


def _scrape_twitter(section: bs4.element.Tag) -> Twitter:
  def get_url() -> typing.Optional[str]:
    elm = section.find(class_='officialTwitter')
    return elm.get('href') if elm else None
  
  def get_username(url: str) -> typing.Optional[str]:
    ptn = re.compile(
      r'^.*twitter.com\/(intent\/.*=)?(.*[^\/])\/?$',
    )
    m = re.match(ptn, url)
    return m.groups()[-1]
  
  url = get_url()
  username = None if url is None else get_username(url)
  return Twitter(username)
