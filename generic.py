from string import ascii_lowercase, ascii_uppercase, digits, punctuation
 
from secrets import randbelow, choice

from random import randint 

generic = []

def upperCase():
     generic.insert(randbelow(5), choice(ascii_uppercase))
def lowCase(): 
     generic.insert(randbelow(3), choice(ascii_lowercase))
def punctuation(): 
     generic.insert(6,choice('!@#@$%&^*'))
def numero():
     generic.insert(randbelow(7), choice(digits))

print('write into console ')

def permutate(p):
	if p == 1: 
	   recargar = randint(7,11) 
	elif p == 2: 
	   recargar = randint(12,17)
	else:
	   recargar = randint(17,25) 

for i in range(int(recargar)): 
    lowCase()
    punctuation()
    upperCase()
    numero()
    pass 
phrase = ''   
for elements in generic: 
    phrase += elements
    pass 

try: 
    import pyperclip as clip

    clip.copy(phrase)
    print('the sequence is copied to the clipboard')
    if recargar >= 0: 
	recargar =  recargar
except:
    print('check read me later' )
