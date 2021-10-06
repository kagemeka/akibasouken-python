import sys 
import typing 


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/../..')

set_globals()
sys.path.append(f'{root}/src')
from lib.akibasouken.scrape import (
  scrape_current_animes,
)


def test_scrape_curren_animes() -> typing.NoReturn:
  for anime in scrape_current_animes():
    print(anime)


if __name__ == '__main__':
  test_scrape_curren_animes()
  