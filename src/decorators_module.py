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



def show_main_menu(res_word: str, word_history: list, attempts: int, letter_colors: dict) -> None:
    print(f"{'_' * 10}Wordle{'_' * 10}")
    print(f"Attempts:")
    print(''.join(res_word))
    for word in word_history:
        for letter in word:
            print((letter_colors[letter] + letter + Back.RESET + Fore.RESET), end='')
        print()
   
    print("Letters: " + ' '.join([color + letter + Back.RESET + Fore.RESET for letter, color in letter_colors.items()]))