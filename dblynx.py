import redis
import keyring
import os
import time
import json 
import uuid






class LocalStrategy():
    def __init__(self, args):
        self.data = keyring
        

    def get(self, id):
        if not self.data.get_password(id):
            return False
        else:
            return self.data.get_password(id)

    def set(self, args):
        self.data.set_password(args.get('username'), args.get('password'), args.get('email'))
        return 

    def delete(self, key):
        return self.data.delete(key)

    def keys(self):
        return self.data.keys()   
    
class RemoteStrategy():
    def __init__(self, args):
        try:
            redis.connection.Connection(args.get('uri'), args.get('port'), args.get('dbnum'))
            self.online = True
        except redis.ConnectionError:
            self.online = False
        self.remotedb = redis.Redis(host= args.get('uri'), port= args.get('port'), db= args.get('dbnum'))

    async def get(self, id):
        return await self.remotedb.get(id)

    def set(self, args):
        return self.remotedb.set(args.get('id'), args.get('username'), args.get('password'))

    def delete(self, key):
        return self.remotedb.delete(key)

    def keys(self):
        return self.remotedb.keys()
    
class Strategy(LocalStrategy, RemoteStrategy):
    def __init__(self, args):
        super().__init__(args)
        self.username = args.get('db_username')
        self.remotedb = redis.Redis(host= args.get('uri'), port= args.get('port'), db= args.get('dbnum'))
        self.local = LocalStrategy()

    async def get(self, id):
        if LocalStrategy.get(id):
            return LocalStrategy.get(id)
        elif RemoteStrategy.online: 
            await RemoteStrategy.get(id)

        

    async def set(self, args):
        while RemoteStrategy.online:
            await RemoteStrategy.set()
            await LocalStrategy.set()
        
        return 0
    

        

    async def delete(self, id):
        while RemoteStrategy.online:
            RemoteStrategy.delete(id)
            LocalStrategy.delete(id)


    def keys(self):
        return self.store.keys