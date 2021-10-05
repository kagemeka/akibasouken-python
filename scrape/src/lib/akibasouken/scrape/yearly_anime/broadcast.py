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
    for elm in elms: broadcasts.append(_get_unit(elm))

  def _get_unit(elm: bs4.element.Tag) -> Broadcast:
    elms = elm.find_all('span')
    if not elms: return
    channel = elms[0].text
    schedule = None if len(elms) < 2 else elms[1].text
    return Broadcast(channel, schedule)

  broadcasts = []
  get_streams()
  get_others()   
  return broadcasts


# class ScrapeBroadcast():

#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> typing.List[Broadcast]:
#     self.__section = section
#     self.__scrape()
#     return self.__broadcasts
  

#   def __get_streams(
#     self,
#   ) -> typing.NoReturn:
#     elm = self.__section.find(
#       class_='dogaLink',
#     )
#     if elm is None: return
#     for a in elm.find_all('a'):
#       channel = a.text
#       bc = Broadcast(channel)
#       self.__broadcasts.append(
#         bc,
#       )


#   def __get_others(
#     self,
#   ) -> typing.NoReturn:
#     elm = self.__section.find(
#       class_='schedule',
#     )
#     if elm is None: return
#     elms = elm.find_all('td')
#     for elm in elms:
#       self.__get_unit(elm)
 

#   def __get_unit(
#     self,
#     elm: bs4.element.Tag,
#   ) -> Broadcast:
#     elms = elm.find_all('span')
#     if not elms: return
#     channel = elms[0].text
#     schedule = (
#       None if len(elms) < 2
#       else elms[1].text
#     )
#     bc = Broadcast(
#       channel,
#       schedule,
#     )
#     self.__broadcasts.append(
#       bc,
#     )


#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     self.__broadcasts = []
#     self.__get_streams()
#     self.__get_others()