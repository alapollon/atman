import jellyfish
import redis 
from email_validator import validate_email, EmailNotValidError



def checkEmail(self, email_address):
        try:
            validate_email(email_address, check_deliverability=True)
            return True
        except EmailNotValidError as e:
            print(str(e))
            return False

def ifEmail(self, email):
        print("probing email")
        if "@" in email:
            return True
        else:
            return False
         

class EmailFilter():
    def __init__(self, args):
        self.email = args.get('email') 
        self.valid = args.get('validity')
        self.domain = args.get('domain')
    
    if self.user_input_email:
        try:
            validate_email(self.user_input_email, check_deliverability=True)

        except EmailNotValidError as e:
            print(str(e))
    
        

mxvalidator = EmailFilter(email = (), validity = ifEmail(()), domain = (()))