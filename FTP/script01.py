#!/usr/bin/env python
import os
import sys
import hashlib
import getpass
import re
p = getpass.getpass()
print ("Sua senha: "), p
hashpass = hashlib.md5(p.encode('utf8')).hexdigest()
print (hashpass)

with open('/home/opera/FTP/roles/ftp/vars/main.yml') as f:
   x = f.read()
   result = x.replace('$1$p3qInU3o$Cb/Z1WiisSL2YBRw0a7Oj.',hashpass) 
   print (result)
