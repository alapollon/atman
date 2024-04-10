import pytest
 
from aa import Index, permutate, recargar 

def test_defaults(): 
    permutate("randomize") 
    assert type(Index().array) is type([ 0, " a" ]) and type(Index().phrase) == type("a string")
def test_permutate():  
    permutate('randomize')
    phrase = Index().phrase
    assert len(phrase) is recargar 
