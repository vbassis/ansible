#!/usr/bin/env python
import os
import sys
import re
import hashlib
import getpass

usuario = raw_input("Entre com o nome de usuario: ")
print 'Entre com a senha: '
p = getpass.getpass()
print ("Sua senha: "), p
hashpass = hashlib.md5(p.encode('utf8')).hexdigest()
print (hashpass)
path = raw_input("Entre com o caminho: ")

with open('/home/opera/FTP/roles/ftp/vars/main.yml','r+') as f:
  x = f.read()
  w = re.split("\s",x)
  novo1 = w[2]
  novo2 = w[6]
  novo3 = w[10]
  print (x)
  result1 = re.sub(novo1,usuario,x)
  result2 = result1.replace(novo2,hashpass) 
  result3 = re.sub(novo3,path,result2)
  final = result3
  f.seek(0)
  f.write(final)
  f.truncate()
  print (final)

