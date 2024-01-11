from random import choice
from colorama import init, Fore, Back


def get_random_word() -> str:
    with open(r'database\words.txt', 'r',) as file:
         word = choice(file.read().split())
    
    return word

def update_user_word(input_word: str, random_word, res_word: str):
    for i in range(5):
        if input_word[i] == random_word[i]:
            res_word[i] = random_word[i]
    return res_word 

def word_in_database(input_word: str) -> bool: 
    with open(r'database\words.txt', 'r',) as file:
        return input_word in file.read()
    
def update_colors(letter_colors: dict, input_word: str,
                  res_word: str, random_word: str) -> dict:
    for i in range(5):
        if input_word[i] == random_word[i]:
            letter_colors[input_word[i]] = Back.GREEN
        elif input_word[i] in random_word:
            letter_colors[input_word[i]] = Back.YELLOW + Fore.RED
        else:
            pass
    return letter_colors

def save_color_fiw(letter_colors: dict, word_history: dict, input_word: str, random_word: str) -> dict:
    random_word = list(random_word)
    for letter in input_word:
        if letter in random_word:
            word_history[input_word] += letter_colors[letter] + letter + Back.RESET + Fore.RESET
            random_word[random_word.index(letter)] = None
        else:
            word_history[input_word] += letter
    
    return word_history

