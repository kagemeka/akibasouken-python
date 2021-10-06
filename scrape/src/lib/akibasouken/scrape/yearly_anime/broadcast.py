import bs4 
import dataclasses
import typing


@dataclasses.dataclass
class Broadcast():
  channel: str
  schedule: typing.Optional[str] = None
  url: typing.Optional[str] = None



def _scrape_broadcast(section: bs4.element.Tag) -> Broadcast:
  def get_streams() -> typing.NoReturn:
    elm = section.find(class_='dogaLink')
    if elm is None: return
    for a in elm.find_all('a'):
      channel = a.text
      broadcasts.append(Broadcast(channel))

  def get_others() -> typing.NoReturn:
    elm = section.find(class_='schedule')
    if elm is None: return
    elms = elm.find_all('td')
    for elm in elms: _get_unit(elm)

  def _get_unit(elm: bs4.element.Tag) -> Broadcast:
    elms = elm.find_all('span')
    if not elms: return
    channel = elms[0].text
    schedule = None if len(elms) < 2 else elms[1].text
    return broadcasts.append(Broadcast(channel, schedule))

  broadcasts = []
  get_streams()
  get_others()   
  return broadcasts
