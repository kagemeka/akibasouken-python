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
import boto3


class AdamAkibasouken():

  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__scrape()
    self.__to_dataframe()
    self.__add_timestamp()
    self.__store()
    self.__upload()

  

  def __init__(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    self.__dt = dt 
    date = dt.date()
    self.__save_path = (
      f'/tmp/'
      'akibasouken.csv'
    )
    self.__upload_path = (
      f'akibasouken/{date}/'
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
  

  def __upload(
    self,
  ) -> typing.NoReturn:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    obj = bucket.Object(
      self.__upload_path,
    )
    obj.upload_file(
      self.__save_path,
    )
  