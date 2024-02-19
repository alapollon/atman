from string import ascii_lowercase, ascii_uppercase, digits, punctuation
 
from secrets import randbelow, choice


generic = []

def upperCase():
    return generic.insert(randbelow(5), choice(ascii_uppercase))
def lowCase(): 
    return generic.insert(randbelow(3), choice(ascii_lowercase))
def punctuation(): 
    return generic.insert(6,choice('!@#@$%&^*'))
def numero():
    return generic.insert(randbelow(7), choice(digits))


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