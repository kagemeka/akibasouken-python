import bs4 
import requests
import typing
import datetime
import tqdm 
from .yearly_anime import YearlyAnime, scrape_yearly_anime



def scrape_current_animes() -> typing.Iterator[YearlyAnime]:
  SEASON = ('winter', 'spring', 'summer', 'autumn')
  BASE_URL = 'https://akiba-souken.com/anime/'

  def _calc_seasons() -> typing.Tuple[str, str]:
    dt = datetime.datetime.now()
    i = dt.month // 3 % 4
    return (SEASON[i], SEASON[(i - 1) % 4])
  
  def compute_urls() -> typing.Iterator[str]:
    return (f'{BASE_URL}{s}' for s in _calc_seasons())
  
  def make_soup(url: str) -> bs4.BeautifulSoup:
    response = requests.get(url)
    return bs4.BeautifulSoup(response.content, 'html.parser')
  
  for url in compute_urls():
    print(url)
    soup = make_soup(url)
    section = soup.find(id='contents')
    animes = section.find_all(class_='itemBox')
    for anime in tqdm.tqdm(animes): 
      yield scrape_yearly_anime(anime)

