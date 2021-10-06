import bs4 
import dataclasses
import re
import typing
import unicodedata 
import datetime 
import logging



@dataclasses.dataclass 
class Metadata():
  title: str 
  media: str
  year: int
  season: typing.Optional[int] = None
  date: typing.Optional[datetime.datetime.date] = None 
  official_site: typing.Optional[str] = None
  copyright: typing.Optional[str] = None



def _scrape_metadata(soup: bs4.BeautifulSoup) -> Metadata:  
  def get_title_media() -> typing.Tuple[str, str]:
    section = soup.find(class_='itemTitle')
    title = section.find('h1').text
    media = section.find(class_='category').text
    return title, media 

  def get_year_season() -> typing.Tuple[
    (typing.Optional[str], ) * 2
  ]:
    section = soup.find(class_='info_main')
    url = section.find('dd').find('a').get('href')
    ptn = re.compile(r'^.*season=(\d+).*$')
    m = re.match(ptn, url)
    season = m.group(1) if m else None
    ptn = re.compile(r'^.*year=(\d+).*$')
    m = re.match(ptn, url)
    year = m.group(1) if m else None
    return year, season
    
  def get_date() -> typing.Optional[datetime.datetime]:
    s = soup.find(class_='info_main').find_all('dd')[1].text
    s = unicodedata.normalize('NFKD', s)
    s = s.rstrip('~')
    try:
      dt = datetime.datetime.strptime(s, '%Y年%m月%d日')
      date = dt.date()
    except Exception as e:
      logging.error(e)
      date = None
    return date

  def get_official_site() -> typing.Optional[str]:
    elm = soup.find(class_='specBox').find('a')
    return elm.get('href') if elm else None 
  
  def get_copyright() -> typing.Optional[str]:
    elm = soup.find(class_='copyright')
    return elm.text if elm else None
  
  return Metadata(
    *get_title_media(),
    *get_year_season(),
    get_date(),
    get_official_site(),
    get_copyright(),
  )


