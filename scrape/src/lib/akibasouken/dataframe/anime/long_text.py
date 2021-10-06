import dataclasses 
import pandas as pd
from lib.akibasouken.scrape.anime import Anime


def long_text_to_df(anime: Anime) -> pd.DataFrame:
  data = {
    'anime_id': anime.anime_id,
    **dataclasses.asdict(anime.long_text),
  }
  return pd.Series(data).to_frame().T
