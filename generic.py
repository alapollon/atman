from string import ascii_lowercase, ascii_uppercase, digits, punctuation
 
from secrets import randbelow, choice

from random import randint 

generic = []
ii = 0
def upperCase():
     generic.insert(randbelow(5), choice(ascii_uppercase))
def lowCase(): 
     generic.insert(randbelow(3), choice(ascii_lowercase))
def punctuation(): 
     generic.insert(6,choice('!@#@$%&^*'))
def numero():
     generic.insert(randbelow(7), choice(digits))
print('write into console ')
async def permutate(i):
     if i == 1: 
         ii = (randint(7,11)) 
     elif i == 2: 
          ii = (randint(12,17))
     else:
          ii = (randint(17,25))
for i in range(ii): 
    lowCase()
    punctuation()
    upperCase()
    numero()
    pass 
phrase = ''   
for elements in generic: 
    phrase += elements
    pass 


