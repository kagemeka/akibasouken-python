import typing
from lib.adam import update_current_animes


def main():
  update_current_animes()



def lambda_handler(event, context) -> typing.NoReturn:
  update_current_animes()



if __name__ == '__main__':
  main()