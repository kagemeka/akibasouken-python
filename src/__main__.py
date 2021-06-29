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




@dataclasses.dataclass
class Score():
  satisfaction: float
  stroy: float
  originality: float
  drawing: float
  direction: float
  charactor: float 
  voice_actor: float
  sound: float
  song: float



class ScrapeScore():
  ...

  def __call__(
    self,
    anime_id: int,
  ) -> Score:
    self.__id = anime_id

  
  def __scrape():
    ...



def main():
  site_url = (
    "https://akiba-souken.com"
  )
  season = "autumn"
  path = f'anime/{season}'

  tg_url = (
    f'{site_url}/{path}'
  )
  print(tg_url)
  res = requests.get(tg_url)
  soup = bs4.BeautifulSoup(
    res.content,
    "html.parser",
  )
  # print(soup.prettify())
  header = soup.find("h1").text
  print(header)

  animes = soup.find(
    id='contents',
  ).find_all(
    class_='itemBox',
  )

  scrape = ScrapeAnime()

  for anime in animes:
    try:
      meta = scrape(anime)
    except:
      continue
    staff = unicodedata.normalize(
      'NFKD', meta.staff,
    )
    pprint(staff.split())




  # cols = ["作品名","放送開始日","スタッフ","公式サイト","Link","公式Twitter","URL"]
  # anime_df = pd.DataFrame(anime_infos,columns=cols)
  # # 出力
  # anime_df.to_csv(f"data/{header}.csv",index=False)


  # anime_df.to_csv(f"../../twitter/data/output/{header}.csv",index=False)



if __name__ == '__main__':
  main()


'''TODO 
title 
on air date
'''