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
    word_history = ['','']
    input_word = ''
    res_word = '?????'
    attempts = 0
    while attempts <= 6:
        dm.show_main_menu(res_word, word_history, attempts, letter_colors)
        input_word = input('Type a word')
        

if __name__ == '__main__':
    main()