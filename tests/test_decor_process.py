from colorama import init, Fore
a = {'a': '', 'b': ''}
init(autoreset=True)
a['b'] += Fore.BLACK
a['a'] += 'q'
print(a)