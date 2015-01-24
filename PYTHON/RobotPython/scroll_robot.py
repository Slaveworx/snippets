# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time as t

""" 
ESTE SCRIPT AUTOMATIZA A LEITURA DE PDF'S E PAGINAS WEB
Slaveworx - Tiago Galvão 2015 - Criado por mera preguiça
de fazer scroll quando estou a ler ebooks.
'"""
######################################################

m = PyMouse()

while True:
	m.scroll(vertical=-1)
	t.sleep(8)
	
