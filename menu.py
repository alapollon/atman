 # todo: research and configure UI 
import base64 
import binascii
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class UserInputs:
    def __init__(self, token, username, password, email, url, nature):
        self.token = token
        self.username = username
        self.user_input_password = password
        self.email = email
        self.url = url
        self.natue = nature # drop down selection of profile type 
        return token, username, password, email, url
        
    def probeToken(self, token):
        print("probing token ")
        try: 
            base64.b64decode(token, validate=True)
            return True
        except binascii.Error:
            return False
    
    def checkEmail(self, email):
        print("probing email")
        if "@" in email:
            return True
        else:
            return False
        

