from colorama import init, Fore, Back
from functools import wraps
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
                 word_history: list, res_word: str):
  print(attempts)
  print(input_word)
  print(res_word)
  print(word_history)
  