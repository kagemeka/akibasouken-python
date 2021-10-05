import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Twitter():
  username: typing.Optional[str] = None


def _scrape_twitter(section: bs4.element.Tag) -> Twitter:
  def get_url() -> typing.Optional[str]:
    elm = section.find(class_='officialTwitter')
    return elm.get('href') if elm else None
  
  def get_username(url: str) -> typing.Optional[str]:
    return url.split('/')[-1]
  
  url = get_url()
  username = None if url is None else get_username(url)
  return Twitter(username)


# class ScrapeTwitter():  
#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> Twitter:
#     self.__section = section
#     self.__scrape()
#     return self.__twitter
  
  
#   def __get_url(
#     self,
#   ) -> typing.NoReturn:
#     elm = self.__section.find(
#       class_='officialTwitter',
#     )
#     self.__url = (
#       elm.get('href') if elm
#       else None
#     )
  

  # def __get_username(
  #   self,
  # ) -> typing.NoReturn:
  #   self.__username = (
  #     self.__url.split('/')[-1]
  #     if self.__url else None
  #   )


  # def __scrape(
  #   self,
  # ) -> typing.NoReturn:
  #   self.__get_url()
  #   self.__get_username()
  #   self.__twitter = Twitter(
  #     self.__username,
  #   )