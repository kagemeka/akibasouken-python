import selenium 
import requests

import time
# import numpy as np
import bs4
import requests
import pandas as pd
import json
import re
from pprint import (
  pprint,
)

import unicodedata

class ScrapeAnimes():
  

  def __calc_season(
    self,
  ):
    season = 'autumn'
    self.__saeson = season
    ...


  def __call__(
    self,
  ):
    ...


  
  

  def __init__(
    self,
  ):
    self.__site_utl = (
      'https://'
      'akiba-souken.com/'
    )
    self.__calc_season()


    # ... 


import dataclasses 









# class ScrapeAnime():
  
#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> Metadata:
#     self.__section = section
#     self.__scrape()
#     return self.__meta

#   def __scrape(
#     self,
#   ):
#     section = self.__section
#     id_ = section.get('id')
#     title = section.find(
#       class_='mTitle',
#     ).find('h2').text
#     onair_date = section.find(
#       class_='firstDate',
#     ).text
#     staff = section.find(
#       class_='staff',
#     ).text
#     site = section.find(
#       class_='officialSite'
#     ).get('href')
#     twitter = section.find(
#       class_='officialTwitter',
#     ).get('href')
#     self.__meta = Metadata(
#       id_,
#       title,
#       onair_date,
#       staff,
#       site,
#       twitter,
#     )






class ScrapeComingAnimes():
  ...




from \
  lib.akibasouken \
  .scrape.anime \
import (
  ScrapeAnime,
)
from \
  lib.akibasouken \
  .scrape.yearly_anime \
import (
  ScrapeTwitter,
)




import bs4 
import dataclasses
import re
import typing
from typing import (
  Optional,
)






def main():
  site_url = (
    "https://akiba-souken.com"
  )

  id_ = 21435
  id_ = 21397
  id_ = 21478
  id_ = 1618
  id_ = 21466
 
 
  url = (
    f'{site_url}/anime/{id_}'
  )
  response = requests.get(url)
  soup = bs4.BeautifulSoup(
    response.content,
    'html.parser',
  )

  scrape = ScrapeAnime()
  pprint(scrape(id_))

  url = (
    f'{site_url}/anime/spring'
  )

  response = requests.get(url)
  soup = bs4.BeautifulSoup(
    response.content,
    'html.parser',
  )

  animes = soup.find(
    id='contents',
  ).find_all(
    class_='itemBox',
  )
  scrape = ScrapeTwitter()
  for anime in animes:
    # print(anime)
    pprint(scrape(anime))
    break
    # break





if __name__ == '__main__':
  main()

