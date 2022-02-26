from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random.random import randint
import keys

(g,n)=keys.MODP160
kab=None
kba=None

def envoie(s,qui,quoi):
    s.send('{}: {}\n'.format(qui,quoi.hex()).encode())

def recoit(s):
    data=s.recv()
    st=data.index(b' ')
    return bytes.fromhex(data[st+1:-1].decode())

def start_alice(s):
   "invoquÃ© avant toute opÃ©ration chez alice"
   global kab,kba
   # DH
   a=randint(0,n)
   x=pow(g,a,n)
   envoie(s,'alice',x.to_bytes(128,'big'))
   y=int.from_bytes(recoit(s),'big')
   # secret partagÃ©
   k=pow(y,a,n).to_bytes(128,'big')
   # dÃ©rivation de clÃ©s
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest()
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest()

def send_alice(s,data):
   "invoquÃ© pour envoyer un message cÃ´tÃ© alice"
   cipher=AES.new(kab, AES.MODE_CTR, nonce=keys.nonce()[:8])
   assert len(cipher.nonce)==8
   c=cipher.encrypt(data)
   msg=cipher.nonce+c
   envoie(s,'alice',msg)

def recv_alice(s):
   "invoquÃ© pour recevoir un message cÃ´tÃ© alice"
   msg=recoit(s)
   nonce=msg[:8]
   c=msg[8:]
   cipher=AES.new(kba, AES.MODE_CTR, nonce=nonce)
   data=cipher.decrypt(c)
   return data

def start_bob(s):
   "invoquÃ© avant toute opÃ©ration chez bob"
   global kab,kba
   # DH
   b=randint(0,n)
   y=pow(g,b,n)
   envoie(s,'bob',y.to_bytes(128,'big'))
   x=int.from_bytes(recoit(s),'big')
   # secret partagÃ©
   k=pow(x,b,n).to_bytes(128,'big')
   # dÃ©rivation de clÃ©s
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest()
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest()

def send_bob(s,data):
   "invoquÃ© pour envoyer un message cÃ´tÃ© alice"
   cipher=AES.new(kba, AES.MODE_CTR, nonce=keys.nonce()[:8])
   assert len(cipher.nonce)==8
   c=cipher.encrypt(data)
   msg=cipher.nonce+c
   envoie(s,'bob',msg)

def recv_bob(s):
   "invoquÃ© pour recevoir un message cÃ´tÃ© alice"
   msg=recoit(s)
   nonce=msg[:8]
   c=msg[8:]
   cipher=AES.new(kab, AES.MODE_CTR, nonce=nonce)
   data=cipher.decrypt(c)
   return data