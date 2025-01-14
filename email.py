import jellyfish
import redis 

class EmailFilter():
    def __init__(self, email):
        self.input_email = email
        