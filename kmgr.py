import pwgen
import dblynx
import base64
import binascii
import os

def __init__(self, **kwargs):
    self.worldcoin = kwargs.get('worldcoin') 
    self.atman_token = kwargs.get('atman_token')

def probeToken(self, token):
        print("probing token ")
        try: 
            base64.b64decode(token, validate=True)
            return True
        except binascii.Error:
            return False