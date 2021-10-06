import bs4
import dataclasses
import re
import typing
import itertools
import unicodedata




@dataclasses.dataclass
class Staff():
  name: str
  role: str



def _scrape_staff(
  soup: bs4.BeautifulSoup,
) -> typing.List[Staff]:
  def  get_staff_text() -> str:
    section = soup.find(class_='staff')
    if section is None: return ''
    staff = section.find('dd').text
    original = soup.find(class_='specBox').find(
      'table',
    ).find_all('td')[0].text
    s = f'{original} {staff}'
    s = ' '.join(s.split())
    s = unicodedata.normalize('NFKC', s)
    return s 

  def split_staff_text(s: str) -> typing.List[str]:
    ptn = re.compile(r'[^:、() ]*:[^:、() ]*')
    return re.findall(ptn, s)

  def compute_combinations(chunk: str):
    m = map(lambda s: re.split(r'/|・', s), chunk.split(':'))
    return itertools.product(*m)
  
  combs = itertools.chain.from_iterable([
    compute_combinations(chunk)
    for chunk in split_staff_text(get_staff_text())
  ])
  return [Staff(name, role) for role, name in combs]

