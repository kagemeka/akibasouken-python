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



from \
  lib.akibasouken.scrape \
  .coming_animes \
import (
  ScrapeComingAnimes,
)






def main():
  site_url = (
    "https://akiba-souken.com"
  )

  id_ = 21435
  id_ = 21397
  id_ = 21478
  id_ = 1618
  id_ = 21466
  # id_ = 21296
 
  # url = (
  #   f'{site_url}/anime/{id_}'
  # )
  # response = requests.get(url)
  # soup = bs4.BeautifulSoup(
  #   response.content,
  #   'html.parser',
  # )

  # scrape = ScrapeAnime()
  # pprint(scrape(id_))


  scrape = ScrapeComingAnimes()
  animes = scrape()
  for anime in animes:
    pprint(anime)
    # break
    print()



if __name__ == '__main__':
  main()

