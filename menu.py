 
import consolemenu_py as Console

from generic import permutate

console = Console.MainMenu("Phrase Generator")
console.add_item(Console.FunctionMenuItem("easy",lambda _:permutate(1)))
console.add_item(Console.FunctionMenuItem("random",lambda _:permutate(2)))
console.add_item(Console.FunctionMenuItem("vaariant",lambda _:permutate()))