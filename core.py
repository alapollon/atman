import abc
import base64 
import binascii
import cryptex

class Credential(abc.ABC):
    def __init__(self, args):
        self._username = args.get('username')
        self._password = args.get('password')
        self._email = args.get('email')
        self._url = args.get('url')
        self._kind = args.get('kind')
        self._id = args.get('id')
        self._ssh_key = args.get('ssh_key')
        self._encryptor = args.get('encryption_key')

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        new_email_domain = set(value.split('@')[1])
        new_email_identity = set(value.split('@')[0])
        self._email = f"{new_email_identity}@{new_email_domain}"

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def ssh_key(self):
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, value):
        self._ssh_key = value

    @property
    def encryptor(self):
        return self._encryptor

    @encryptor.setter
    def encryptor(self, value):
        self._encryptor = value


cc = Credential()