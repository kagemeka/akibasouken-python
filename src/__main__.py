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


@dataclasses.dataclass
class Cast():
  anime_id: int
  cast_id: int
  name: str



class ScrapeCast():
  ...




@dataclasses.dataclass 
class Metadata():
  anime_id: int
  title: str
  onair_date: str
  staff: str
  site_url: str 
  twitter_url: str




class ScrapeMetadata():
  ...







class ScrapeAnime():
  
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> Metadata:
    self.__section = section
    self.__scrape()
    return self.__meta

  def __scrape(
    self,
  ):
    section = self.__section
    id_ = section.get('id')
    title = section.find(
      class_='mTitle',
    ).find('h2').text
    onair_date = section.find(
      class_='firstDate',
    ).text
    staff = section.find(
      class_='staff',
    ).text
    site = section.find(
      class_='officialSite'
    ).get('href')
    twitter = section.find(
      class_='officialTwitter',
    ).get('href')
    self.__meta = Metadata(
      id_,
      title,
      onair_date,
      staff,
      site,
      twitter,
    )






class ScrapeComingAnimes():
  ...




from \
  lib.akibasouken \
  .scrape.anime \
import (
  ScrapeStaff,
  ScrapeVoiceActor,
  ScrapeScore,
  ScrapeMetadata,
  ScrapeStudio,
  ScrapeGenre,
  ScrapeLongText,
  ScrapeTag,
)



import bs4 
import dataclasses
import re
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass 
class LongText():
  commentary: str
  overview: str


@dataclasses.dataclass 
class Genre():
  genre_id: int
  name: str





def main():
  site_url = (
    "https://akiba-souken.com"
  )
  # season = "autumn"
  # path = f'anime/{season}'

  # tg_url = (
  #   f'{site_url}/{path}'
  # )
  # print(tg_url)
  # res = requests.get(tg_url)
  # soup = bs4.BeautifulSoup(
  #   res.content,
  #   "html.parser",
  # )
  # # print(soup.prettify())
  # header = soup.find("h1").text
  # print(header)

  # animes = soup.find(
  #   id='contents',
  # ).find_all(
  #   class_='itemBox',
  # )

  # scrape = ScrapeAnime()

  # for anime in animes:
  #   try:
  #     meta = scrape(anime)
  #   except:
  #     continue
  #   staff = unicodedata.normalize(
  #     'NFKD', meta.staff,
  #   )
  #   pprint(staff.split())

  id_ = 21435
  id_ = 21397
  id_ = 21478
  id_ = 1618
  url = (
    f'{site_url}/anime/{id_}'
  )
  response = requests.get(url)
  soup = bs4.BeautifulSoup(
    response.content,
    'html.parser',
  )


  scrape = ScrapeStaff()
  staffs = scrape(soup)
  pprint(staffs)

  scrape = ScrapeVoiceActor()
  actors = scrape(soup)
  pprint(actors)


  scrape = ScrapeScore()
  score = scrape(soup)
  pprint(score)


  scrape = ScrapeMetadata()
  metadata = scrape(soup)
  pprint(metadata)


  scrape = ScrapeStudio()
  studio = scrape(soup)
  pprint(studio)

  scrape = ScrapeGenre()
  genres = scrape(soup)
  pprint(genres)

  scrape = ScrapeLongText()
  long_txt = scrape(soup)
  pprint(long_txt)

  scrape = ScrapeTag()
  tags = scrape(soup)
  pprint(tags)




if __name__ == '__main__':
  main()


'''TODO 
title 
on air date
'''