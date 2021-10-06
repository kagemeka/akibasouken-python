import typing
import pandas as pd
import datetime
from lib.akibasouken.scrape.current_animes import (
  scrape_current_animes,
)
from lib.akibasouken.scrape.yearly_anime import YearlyAnime
from lib.akibasouken.dataframe.anime import  (
  metadata_to_df
)
from lib.akibasouken.dataframe.yearly_anime import (
  twitter_to_df,
)
from lib.aws_util.s3.upload import upload_to_s3



def update_current_animes() -> typing.NoReturn:
  animes = scrape_current_animes()
  df = pd.concat(
    map(make_dataframe, animes),
    ignore_index=True,
  )
  _store_to_s3(df)


def make_dataframe(anime: YearlyAnime) -> pd.DataFrame:
  meta = metadata_to_df(anime)
  twitter = twitter_to_df(anime)
  return meta.merge(twitter, how='left', on='anime_id')


def _store_to_s3(df: pd.DataFrame) -> typing.NoReturn:
  dt = datetime.datetime.now()
  save_path = f'/tmp/data.csv'
  bucket = 'av-adam-store'
  upload_obj = f'akibasouken/meta.csv'
  df['updated_at'] = dt.date()
  print(df)
  df.to_csv(save_path, index=False)
  upload_to_s3(bucket, upload_obj, save_path)