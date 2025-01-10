
from buoyance import generator

from string import ascii_lowercase, ascii_uppercase, digits
 
from secrets import randbelow, choice

from random import randint 


gblock = generator.generative_block

def upperCase(): 
     gblock.insert(randbelow(5), choice(ascii_uppercase))
def lowCase(): 
     gblock.insert(randbelow(3), choice(ascii_lowercase))
def punctuation(self): 
     gblock.insert(6,choice('!@#$%&^'))
def numero():
     gblock.insert(randbelow(7), choice(digits))

