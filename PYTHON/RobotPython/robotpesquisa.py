# -*- coding: utf-8 -*-
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time

""" 
ESTE SCRIPT PESQUISA AUTOMATICAMENTE UMA STRING NO GOOGLE
Slaveworx - Tiago Galvão 2015 - Criado para testar o poder
da biblioteca PyUserInput.
"""


k = PyKeyboard()
m = PyMouse()

print "ROBOT DE PESQUISA"


def escrever():
	k.type_string('Python is great!')
	

def fechar():
	m.click(1356, 38) #clica no botao fechar

def minimizar():
	m.click(1312, 38) #clica no botao minimizar

def pesquisar():	
	m.click(417, 478) #clica na searchbar do google

def go():
	m.click(758, 186)

pesquisar()
time.sleep(2)	
escrever()
time.sleep(2)
go()
time.sleep(4)
fechar()




