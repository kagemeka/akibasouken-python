import selenium
import time
import bs4
import requests
import pandas as pd
import json
import re
from pprint import (
  pprint,
)

import unicodedata  



from \
  lib.akibasouken.scrape \
  .coming_animes \
import (
  ScrapeComingAnimes,
)

import dataclasses
from dataclasses import (
  asdict,
)
import typing
import pandas as pd


from \
  lib.akibasouken.scrape \
  .yearly_anime \
import (
  YearlyAnime,
)


from \
  lib.akibasouken.store \
  .dataframe.anime \
import (
  MetadataToDF,
)

from \
  lib.akibasouken.store \
  .dataframe.yearly_anime \
import (
  TwitterToDF,
)



from datetime import (
  datetime,
)

import os


class AdamAkibasouken():

  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__scrape()
    self.__to_dataframe()
    self.__add_timestamp()
    self.__store()

  

  def __init__(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    self.__dt = dt 
    date = dt.strftime(
      '%Y%m%d',
    )
    self.__save_path = (
      f'/tmp/{date}/'
      'akibasouken.csv'
    )

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__animes = (
      ScrapeComingAnimes()()
    )
  

  def __to_dataframe(
    self,
  ): 
    animes = map(
      self.__anime_to_df,
      self.__animes,
    )
    self.__tbl = pd.concat(
      animes,
      ignore_index=True,
    )


  def __anime_to_df(
    self,
    anime: YearlyAnime,
  ) -> pd.DataFrame:
    meta = MetadataToDF()(
      anime,
    )
    twitter = TwitterToDF()(
      anime,
    )
    twitter.rename(
      columns={
        'url': 'twitter_url',
      }, 
      inplace=True,
    )
    return meta.merge(
      twitter,
      how='left',
      on='anime_id',
    )


  def __add_timestamp(
    self,
  ) -> typing.NoReturn:
    tbl = self.__tbl
    tbl['datetime'] = self.__dt

  

  def __store(
    self,
  ) -> typing.NoReturn:
    path = self.__save_path
    os.makedirs(
      os.path.dirname(path),
      exist_ok=1,
    )
    self.__tbl.to_csv(
      path,
      index=False,
    )
    print(self.__tbl)



def main():
  site_url = (
    "https://akiba-souken.com"
  )


  adam = AdamAkibasouken()
  adam()



if __name__ == '__main__':
  main()