#!/usr/bin/env python
import os
import sys
import re

def altera01():
    with open("/home/opera/DELETEFILES/roles/srv01/vars/main.yml",'r') as f:
        x = f.read()
        print (x)

def altera02(dado1, dado2):
    with open("/home/opera/DELETEFILES/roles/srv01/vars/main.yml",'r') as f:
        x = f.read()
        w = re.split("\s",x)
        resultado1 = w[2]
        resultado2 = w[5]
        final1 = x.replace(resultado1,dado1)
        final2 = final1.replace(resultado2,dado2)
        print (final2) 

def altera03(dado3):
    with open("/home/opera/DELETEFILES/hosts",'r') as f:
        b = f.read()
        final3 = re.sub('(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',dado3,b)
        print (final3)

def main():
    p = raw_input("Entre com o IP: ")
    q = raw_input("Entre com a caminho: ")
    n = raw_input("Entre com o Data: ")
    altera01()
    j = raw_input("Voce gostaria de realizar esta alteracao? Sim(s) ou Nao(n): ")
    if j == "s":
      altera02(q,n)
      altera03(p)
    else:
      altera01()


if __name__ == '__main__':
    main()
