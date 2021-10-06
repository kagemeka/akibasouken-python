import dataclasses
import pandas as pd 
from lib.akibasouken.scrape.yearly_anime import YearlyAnime


def twitter_to_df(anime: YearlyAnime) -> pd.DataFrame:
    data = {
      'anime_id': anime.anime_id,
      **dataclasses.asdict(anime.twitter),
    }
    return pd.Series(data).to_frame().T
