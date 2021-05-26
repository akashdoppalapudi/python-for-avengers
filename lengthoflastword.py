s = input()

words = s.split(' ')
while '' in words:
    words.remove('')

if len(words) == 0:
    print(0)
else:
    print(len(words[-1]))