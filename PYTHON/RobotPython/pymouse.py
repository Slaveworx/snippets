from pykeyboard import PyKeyboard
from pymouse import PyMouse


k = PyKeyboard()
m = PyMouse()

print "ROBOT DE PESQUISA"


def escrever():
	k.tap_key('p')
	k.tap_key('y')
	k.tap_key('t')
	k.tap_key('h')
	k.tap_key('o')
	k.tap_key('n')
	k.tap_key('space')
	k.tap_key('i')
	k.tap_key('s')
	k.tap_key('space')python is powerfull
	k.tap_key('p')
	k.tap_key('o')
	k.tap_key('w')
	k.tap_key('e')
	k.tap_key('r')
	k.tap_key('f')
	k.tap_key('u')
	k.tap_key('l')
	k.tap_key('l')
	

def fechar():
	m.click(1356, 38) #clica no botao fechar

def minimizar():
	m.click(1312, 38) #clica no botao minimizar

def pesquisar():	
	m.click(417, 478) #clica na searchbar do google

def go():
	m.click(758, 186)

pesquisar()	
escrever()
go()
fechar()




