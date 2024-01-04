from random import choice



def get_random_word():
    with open(r'database\words.txt', 'r',) as file:
         word = choice(file.read().split())
    
    return word


def word_in_database(input_word: str) -> bool: 
    pass