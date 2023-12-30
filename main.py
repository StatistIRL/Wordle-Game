import src.decorators_module as dm
import src.logic_module as lm

def main() -> None:
  dm.welcome()
  print('To start playing, press Enter\nFor exit 1 and Enter')
  if input() == '1':
    exit()
  else:
    game()


def game():
  print(1111)
  
if __name__ == '__main__':
  main()