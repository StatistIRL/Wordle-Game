import src.decorators_module as dm
import src.logic_module as lm

def main() -> None:
  dm.welcome()
  print('To start playing, press Enter\nFor exit 1 and Enter')
  if input() == '1':
    exit()
  else:
    game()
 
def game():  # Try to separate the logic and decor into a separate file. game(chosen_word, attempts, res_word, word_history)
  res_word = lm.random_word()
  word_history = ['','','','','','']
  attempts = 0
  user_word = '?????'
  while attempts <= 6:
    input_word = dm.show_results(attempts, word_history, res_word, user_word) 
    process_result = lm.processing(input_word, user_word, word_history, res_word, attempts)
    if process_result:
      user_word, word_history = process_result
      attempts += 1
    else:
      print('The word is not in the database. Try again')
    
if __name__ == '__main__':
  main()