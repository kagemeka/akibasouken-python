
from lib.adam import (
  AdamAkibasouken,
)

# from kgmk.akibasouken

def main():
  site_url = (
    "https://akiba-souken.com"
  )


  adam = AdamAkibasouken()
  adam()



def lambda_handler(
  event,
  context,
):

  main()




if __name__ == '__main__':
  main()