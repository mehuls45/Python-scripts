#! python3
# CussWordScanner

cuss = {'fuck':'****','cunt':'****','asshole':'******','bastard':'*******',
        'fucker':'******','fucking':'*******','bastards':'********',
        'cunts':'*****','assholes':'********'
        }

import pyperclip

text = pyperclip.paste()

words = text.split(' ')

for i in range (len(words)):
    
    word = words[i]
    word = word.lower()

    if word in cuss.keys():
        words[i] = cuss[word]

text = ' '.join(words)
pyperclip.copy(text)
