import dataclasses
import pandas as pd
from .twitter import twitter_to_df


@dataclasses.dataclass
class YearlyAnimeDF():
  metadata: pd.DataFrame
  twitter: pd.DataFrame
  staff: pd.DataFrame
  voice_actor: pd.DataFrame
  studio: pd.DataFrame
  genre: pd.DataFrame
  tag: pd.DataFrame
  broadcast: pd.DataFrame