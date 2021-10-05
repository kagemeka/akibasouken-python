import typing
from lib.adam import AdamAkibasouken


def main():
  site_url = "https://akiba-souken.com"


  adam = AdamAkibasouken()
  adam()



def lambda_handler(event, context) -> typing.NoReturn:

  main()




if __name__ == '__main__':
  main()