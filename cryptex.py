import cryptography
import cryptography.fernet 

# use to copy splice to os clipboard 
from pyperclip import clip


schemes = {}

class cryptex: 
    def __init__(self, void):
        self.input = void
        self.cipher = cryptography.fernet.generate_key()
        pass
    
    def splice(self, plaintext):
        digest = cryptography.fernet(self.cipher)
        return digest.encrypt(plaintext)
        
    def ktrunc(self):
        pass
    