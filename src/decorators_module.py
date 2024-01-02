from colorama import init, Fore, Back

def welcome() -> None:
  print('_' * 30 + 'Wordle-Game' + '_' * 30)
  print('Welcome to the Wordle-Game'.center(71))
  print('Rules:\nYou must guess a word consisting of 5 letters.\nDepending on their location in the word will be colored with a certain color:')
  rule_color()
  
def rule_color() -> None:
  init(autoreset=True)
  print(Back.YELLOW + Fore.RED + '[This color means the letter is in the word, but not in its place.]')
  print(Back.GREEN + '[This color means that the letter is in the word and that it is in the right place.]')
  
def show_results(attempts: int, input_word: str,
                 word_history: list, res_word: str, user_word: str):
  KEYBOARD = ('QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM')
  word_history = ['','','','','','']
  print('-' * 47)
  print('#' * 47)
  print('-' * 47)
  print(' ' * 8 + '|')
  print('Word:' + ' ' * 3 + '|' + ' ' * 5 + f'Attempts: {attempts}')
  print('_' * 8 + '|')
  print(' ' * 8 + '|')
  print(user_word + ' ' * 3 + '|')
  print('_' * 8 + '|')
  for i in range(6):
    print(' ' * 8 + '|')
    print(f'{word_history[i]:8}|' + (' ' * 10 + decor_keyboard(KEYBOARD[i], user_word, res_word, input_word)) if i < 3 else '')
  
  

def decor_keyboard(keyboard_line: str, user_word: str, res_word: str, input_word: str) -> str:
  result = []
  init(autoreset=True)
  for i in keyboard_line:
    if i in user_word:
      result.append(Back.GREEN + i + Back.RESET)
    
    elif i in res_word and input_word:
      result.append(Back.YELLOW + Fore.RED + i + Back.RESET + Fore.RESET)
      
    else:
      result.append(i)
  
  return ' '.join(result)
        
    


