import random

def random_word() -> str:
  with open(r'database\words.txt', 'r', ) as file:
    word = random.choice(file.read().split())
    
    return word
  
  
def processing(input_word: str,user_word: str, 
              word_history: list, res_word: str, attempts: int) -> list:
  
  with open(r'database\words.txt', 'r', ) as file:
    if input_word in file.read():
      for i in range(5):
        if input_word[i] == res_word[i]:
          user_word = list(user_word)
          user_word[i] = res_word[i]
          user_word = ''.join(user_word)
      word_history[attempts] = input_word
      
      return [user_word, word_history]
    else:
     
      return False