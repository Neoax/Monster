# -*- coding: utf-8 -*-

import hashlib
import os
import random

mav = "\033[46m"
bey = "\033[0m"
siy = "\033[40m"
mas = "\033[36m"
kir = "\033[31m"

md5 = False
sha1 = False
sha224 = False
sha256 = False
sha384 = False
sha512 = False

def banner():
       print(mas+"""
      dBBBBBBb  dBBBBP dBBBBb.dBBBBP dBBBBBBP dBBBP dBBBBBb
       '   dB' dBP.BP     dBPBP                         dBP"""+bey+"""
    dB'dB'dB' dBP.BP dBP dBP `BBBBb   dBP   dBBP    dBBBBK
   dB'dB'dB' dBP.BP dBP dBP     dBP  dBP   dBP     dBP  BB
  dB'dB'dB' dBBBBP dBP dBP dBBBBP'  dBP   dBBBBP  dBP  dB'
                                                   Coded by Neoax"""+mas+"""
                                                         v2
       """)

def cracker():
   while True:
      password = ""
      for i in range(random.randint(min, max)):
           password += str(random.choice(list))
      if(md5 == True):
              hashed = hashlib.md5(password).hexdigest()
      elif(sha1 == True):
              hashed = hashlib.sha1(password).hexdigest()
      elif(sha256 == True):
              hashed = hashlib.sha256(password).hexdigest()
      elif(sha224 == True):
              hashed = hashlib.sha224(password).hexdigest()
      elif(sha384 == True):
              hashed = hashlib.sha384(password).hexdigest()
      elif(sha512 == True):
              hashed = hashlib.sha512(password).hexdigest()
      if(hashed == hash):
              print(mav+"[+] "+hash+" - Found - "+hashed+" - "+password+siy)
              exit()
      else:
              print(kir+"["+bey+"-"+kir+"] "+bey+hash+" - Not found - "+hashed+" - "+password)
os.system("clear")
banner()


print(mas+"       ["+bey+"1"+mas+"]"+bey+"-Md5"+mas+"                     ["+bey+"4"+mas+"]"+bey+"-Sha256")
print(mas+"       ["+bey+"2"+mas+"]"+bey+"-Sha1"+mas+"                    ["+bey+"5"+mas+"]"+bey+"-Sha384")
print(mas+"       ["+bey+"3"+mas+"]"+bey+"-Sha224"+mas+"                  ["+bey+"6"+mas+"]"+bey+"-Sha512")

tek = raw_input(mas+"\n|"+bey+"Monster"+mas+": "+bey)
if(tek == "1"):
      md5 = True
elif(tek == "2"):
      sha1 = True
elif(tek == "3"):
      sha224 = True
elif(tek == "4"):
      sha256 = True
elif(tek == "5"):
      sha384 = True
elif(tek == "6"):
      sha512 = True
else:
      print("yanlis secenek girildi!")
os.system("clear")
banner()
hash = raw_input(mas+"hash: "+bey)
kara = raw_input(mas+"karakterler(orn: 2,a,6,c,d,g,9): "+bey)
min = int(raw_input(mas+"minimum karakter sayisi: "+bey))
max = int(raw_input(mas+"maximum karakter sayii: "+bey))
list = kara.split(",")
cracker()
