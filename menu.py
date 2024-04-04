 
import consolemenu 

menu = consolemenu.ConsoleMenu("Phrase Generator","select any permutation")

from generic import permutate

easy = FunctionItem(permutate(1)) 

random = FunctionItem(permutate(2))

variant = FunctionItem(permutate()) 

selection_menu = SelectionMenu([easy,random,variant]) 

menu.append_item(easy, random, variant) 

def display():
	menu.show()

