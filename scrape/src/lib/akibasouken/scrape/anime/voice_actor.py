
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

