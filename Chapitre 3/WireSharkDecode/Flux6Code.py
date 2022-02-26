from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad, unpad
import keys

kab=None
kba=None

def boi(i,n=None):
    if n is not None:
        return i.to_bytes(n,'big')
    else:
        h=hex(i)[2:]
        if len(h)%2 == 1: h='0'+h
        return bytes.fromhex(h)

def iob(b):
    return int.from_bytes(b,'big')

def envoie(s,qui,quoi):
    s.send('{}: {}\n'.format(qui,quoi.hex()).encode())

def recoit(s):
    data=s.recv()
    st=data.index(b' ')
    return bytes.fromhex(data[st+1:-1].decode())

def start_alice(s):
   "invoquÃ© avant toute opÃ©ration chez alice"
   global kab,kba
   # RSA
   key=keys.rsa_alice
   na=key.n
   ea=key.e
   da=key.d
   envoie(s,'alice',boi(na))
   envoie(s,'alice',boi(ea))
   nb=iob(recoit(s))
   eb=iob(recoit(s))
   a=randint(0,nb)
   x=pow(a,eb,nb)
   envoie(s,'alice',boi(x))
   y=iob(recoit(s))
   # secret partagÃ©
   b=pow(y,da,na)
   k=boi(a^b)
   # dÃ©rivation de clÃ©s
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest()
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest()

def send_alice(s,data):
   "invoquÃ© pour envoyer un message cÃ´tÃ© alice"
   cipher=AES.new(kab, AES.MODE_CBC)
   assert len(cipher.iv)==16
   c=cipher.encrypt(pad(data,16))
   msg=cipher.iv+c
   envoie(s,'alice',msg)

def recv_alice(s):
   "invoquÃ© pour recevoir un message cÃ´tÃ© alice"
   msg=recoit(s)
   iv=msg[:16]
   c=msg[16:]
   cipher=AES.new(kba, AES.MODE_CBC, iv=iv)
   data=cipher.decrypt(c)
   return unpad(data,16)

def start_bob(s):
   "invoquÃ© avant toute opÃ©ration chez bob"
   global kab,kba
   # RSA
   key=keys.rsa_bob
   nb=key.n
   eb=key.e
   db=key.d
   na=iob(recoit(s))
   ea=iob(recoit(s))
   envoie(s,'bob',boi(nb))
   envoie(s,'bob',boi(eb))
   x=iob(recoit(s))
   b=randint(0,na)
   y=pow(b,ea,na)
   envoie(s,'bob',boi(y))
   # secret partagÃ©
   a=pow(x,db,nb)
   k=boi(a^b)
   # dÃ©rivation de clÃ©s
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest()
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest()

def send_bob(s,data):
   "invoquÃ© pour envoyer un message cÃ´tÃ© alice"
   cipher=AES.new(kba, AES.MODE_CBC)
   assert len(cipher.iv)==16
   c=cipher.encrypt(pad(data,16))
   msg=cipher.iv+c
   envoie(s,'bob',msg)

def recv_bob(s):
   "invoquÃ© pour recevoir un message cÃ´tÃ© alice"
   msg=recoit(s)
   iv=msg[:16]
   c=msg[16:]
   cipher=AES.new(kab, AES.MODE_CBC, iv=iv)
   data=cipher.decrypt(c)
   return unpad(data,16)