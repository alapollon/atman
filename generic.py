
from aa import __array, permutate, __phrase, recargar

from string import ascii_lowercase, ascii_uppercase, digits
 
from secrets import randbelow, choice

from random import randint 


def upperCase(self): 
     array.insert(randbelow(5), choice(ascii_uppercase))
def lowCase(): 
     array.insert(randbelow(3), choice(ascii_lowercase))
def punctuation(self): 
     array.insert(6,choice('!@#$%&^'))
def numero():
     array.insert(randbelow(7), choice(digits))

if permutate == "easy": 
     recargar = randint(7,11)
elif permutate == "randomize":
     recargar = randint(12,17)
elif permutate == "variable":
     recargar = randint(17,25)
for i in range(recargar): 
     lowCase()
     punctuation()
     upperCase()
     numero()
     pass 
for elements in __array:
     __phrase += elements
try: 
     from pyperclip import clip
     while len(__phrase) == recargar:
          clip.copy(_phrase)

except: 
     print("check readme.rd later ")
     
     