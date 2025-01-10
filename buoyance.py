import abc



class GenerativeIndex(): 
    def __init__(self, ):
        self.generative_block = []
        self.Keyphrase = ""
        self.count = 0
        
    @property
    def block(self, ):
        return self.generative_block
    @property
    def password(self):
        return self.Keyphrase 
    @property
    def iterator(self, i):
        from random import randint
        if i == "2": 
            return randint(7,11)
        elif i == "3":
            return randint(12,17)
        elif i == "4":
            return 
    
        return self.count
    

gen = GenerativeIndex()
