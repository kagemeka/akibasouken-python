
import bs4
import dataclasses
import typing


@dataclasses.dataclass
class VoiceActor:
  name: str
  actor_id: int = None 


def _scrape_voice_actor(
  soup: bs4.BeautifulSoup,
) -> typing.List[VoiceActor]:
  def get_actors_with_id() -> typing.NoReturn:
    for actor in section.find_all('a'):
      name = actor.text
      url = actor.get('href')
      id_ = url.split('/')[-2]
      actor = VoiceActor(name, id_)
      actors.append(actor)

  def get_other_actors() -> typing.NoReturn:
    names = set(a.name for a in actors)
    for name in section.text.split('、'):
      if name in names: continue 
      actor = VoiceActor(name)
      actors.append(actor)    

  section = soup.find(class_='cast')
  actors = []
  if section is None: return actors 
  section = section.find('dd')  
  get_actors_with_id()
  get_other_actors()
  return actors




# class ScrapeVoiceActor():

#   def __call__(
#     self,
#     soup: bs4.BeautifulSoup,
#   ) -> typing.List[VoiceActor]:
#     self.__soup = soup
#     self.__scrape()
#     return self.__actors
  

#   def __get_actors_with_id(
#     self,
#   ) -> typing.NoReturn:
#     section = self.__section
#     actors = section.find_all(
#       'a',
#     )
#     for actor in actors:
#       name = actor.text
#       url = actor.get('href')
#       id_ = url.split('/')[-2]
#       actor = VoiceActor(
#         name,
#         id_,
#       )
#       self.__actors.append(
#         actor,
#       )


#   def __get_other_actors(
#     self,
#   ) -> typing.NoReturn:
#     t = self.__section.text
#     names = set(
#       a.name
#       for a in self.__actors
#     )
#     for name in t.split('、'):
#       if name in names:
#         continue 
#       actor = VoiceActor(name)
#       self.__actors.append(
#         actor,
#       )
    
  
#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     soup = self.__soup
#     self.__actors = []
#     section = soup.find(
#       class_='cast',
#     )
#     if section is None: return
#     section = section.find(
#       'dd',
#     )
#     self.__section = section
#     self.__get_actors_with_id()
#     self.__get_other_actors()