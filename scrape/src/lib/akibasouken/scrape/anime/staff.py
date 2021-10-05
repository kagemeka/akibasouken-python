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











# class ScrapeStaff():
#   def __calc_combinations(
#     self,
#     chunk: str,
#   ):
#     from itertools import (
#       product,
#     )
#     m = map(
#       lambda s: re.split(
#         r'/|・',
#         s,
#       ),
#       chunk.split(':'),
#     )
#     self.__cmbs.append(
#       product(*m),
#     )
    

#   def __call__(
#     self,
#     soup: bs4.BeautifulSoup,
#   ) -> typing.List[Staff]:
#     self.__soup = soup
#     self.__scrape()
#     return [
#       Staff(name, role)
#       for role, name in (
#         self.__staffs
#       )
#     ]
    

#   def  __get_staff_text(
#     self,
#   ):
#     soup = self.__soup
#     section = soup.find(
#       class_='staff',
#     )
#     if section is None:
#       self.__text = ''
#       return
#     staff = section.find(
#       'dd',
#     ).text
#     original = soup.find(
#       class_='specBox',
#     ).find('table').find_all(
#       'td',
#     )[0].text
#     s = f'{original} {staff}'
#     s = self.__rep_whitespaces(
#       s,
#     )
#     s = self.__normalize(s)
#     self.__text = s
  

#   def __normalize(
#     self,
#     s: str,
#   ) -> str:
#     from unicodedata import (
#       normalize,
#     )
#     return normalize('NFKC', s)


#   def __rep_whitespaces(
#     self,
#     s: str,
#   ) -> str:
#     return ' '.join(s.split())


#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     self.__get_staff_text()
#     self.__split_staff_text()
#     self.__cmbs = []
#     for chunk in self.__staffs:
#       self.__calc_combinations(
#         chunk,
#       )
#     from itertools import (
#       chain,
#     )
#     cmbs = chain.from_iterable(
#       self.__cmbs,
#     )
#     self.__staffs = cmbs


#   def __split_staff_text(
#     self,
#   ):
#     ptn = re.compile(
#       r'[^:、() ]*:[^:、() ]*',
#     )
#     self.__staffs = re.findall(
#       ptn,
#       self.__text,
#     )