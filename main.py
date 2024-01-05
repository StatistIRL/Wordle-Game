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
    random_word = lm.get_random_word()
    letter_colors = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '',
               'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '',
               'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '',
               'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': ''}
    word_history = []
    input_word = ''
    res_word = ['?', '?', '?', '?', '?']
    attempts = 0
    while attempts <= 5:
        dm.show_main_menu(res_word, word_history, attempts, letter_colors)
        input_word = input('Type a word: ').upper()
        if lm.word_in_database(input_word):
            word_history.append(input_word)
            lm.update_user_word(input_word, random_word, res_word)
            if '?' not in res_word:
                break
            attempts += 1
            lm.update_colors(letter_colors, input_word, res_word, random_word)
        else:
            print('The word is not in the database. Try again')
    if ''.join(res_word) == random_word:
        print('You Win!!!')
    else:
        print(f'The chosen word was: {random_word}')
        print('You lost!!!')
        another_round()

def another_round() -> None:
    print('Do you want to play again?\nTo start playing, press Enter\nFor exit 1 and Enter')
    if input() == '1':
        exit()
    else:
        game()
    
   
if __name__ == '__main__':
    main()