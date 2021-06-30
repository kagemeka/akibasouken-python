from dataclasses import (
  asdict,
)
import typing
import pandas as pd
from \
  lib.akibasouken.scrape \
  .anime \
import (
  Anime,
)


class LongTextToDF():

  def __call__(
    self,
    anime: Anime,
  ) -> pd.DataFrame:
    anime_id = anime.anime_id
    data = {
      'anime_id': anime_id,
      **asdict(
        anime.long_text,
      ),
    }
    return pd.Series(
      data,
    ).to_frame().T