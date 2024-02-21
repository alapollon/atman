from string import ascii_lowercase, ascii_uppercase, digits, punctuation
 
from secrets import randbelow, choice


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
recargar = input()

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
except:
    print('check read me later' )