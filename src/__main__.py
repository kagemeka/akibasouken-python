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

from lib.adam import (
  AdamAkibasouken,
)



def main():
  site_url = (
    "https://akiba-souken.com"
  )


  adam = AdamAkibasouken()
  adam()



if __name__ == '__main__':
  main()