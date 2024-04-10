 
import consolemenu_py as Console

from generic import permutate

console = Console.MainMenu("Generic Password Generator")
console.add_item(Console.FunctionMenuItem("easy",lambda _:permutate("easy")))
console.add_item(Console.FunctionMenuItem("random",lambda _:permutate("randomize")))
console.add_item(Console.FunctionMenuItem("vaariant",lambda _:permutate("variable")))
