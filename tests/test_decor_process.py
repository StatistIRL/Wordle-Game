m = {'a': '11a'}
l = {'a': 'saa', 'c': 'ad'}
def say_j(l):
    con = 1
    for i in l.keys():
        l[i] = con
        con += 1


say_j(l)
print(l)