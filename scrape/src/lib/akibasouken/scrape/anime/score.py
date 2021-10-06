import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Score():
  satisfaction: float = None
  stroy: float = None
  originality: float = None
  drawing: float = None 
  direction: float = None 
  charactor: float = None 
  voice_actor: float = None 
  sound: float = None 
  song: float = None



def _scrape_score(soup: bs4.BeautifulSoup) -> Score:  
  section = soup.find(class_='evalScore')
  scores = []
  total = section.find('strong').text 
  scores.append(total)
  for s in section.find_all('dd'): scores.append(s.text)
  return Score(*(
    None if s == '-' else float(s) 
    for s in scores
  ))
    
    