import dataclasses
import pandas as pd 
from lib.akibasouken.scrape.anime import Anime


def score_to_df(anime: Anime) -> pd.DataFrame:
    data = {
      'anime_id': anime.anime_id,
      **dataclasses.asdict(anime.score),
    }
    return pd.Series(data).to_frame().T

