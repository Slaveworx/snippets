# -*- coding: utf-8 -*-

from pymouse import PyMouse
import time as t
import Tkinter as tk


""" 
ESTE SCRIPT AUTOMATIZA A LEITURA DE PDF'S E PAGINAS WEB
Slaveworx - Tiago Galvão 2015 - Criado por mera preguiça
de fazer scroll quando estou a ler ebooks.
'"""
######################################################

m = PyMouse()


class Scroll():
	global running
	running = True
	
	def scrolldown(self):
		while running==True:
			m.scroll(vertical=-1)
			t.sleep(8)

	def scrollup(self):
		while running==True:
			m.scroll(vertical=+1)
			t.sleep(8)

	def fastscrolldown(self):
		while running==True:
			m.scroll(vertical=-10)
			t.sleep(1)

	def fastscrollup(self):
		while running==True:
			m.scroll(vertical=10)
			t.sleep(1)
	
	def stop(self):
		running = False
	
	
    
s = Scroll()


####################################################
	
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

	
root = tk.Tk()

root.title("Scroll Robot 1.0")

frameesq = tk.Frame(root)
frameesq.pack( side = "left")

framedir = tk.Frame(root)
framedir.pack( side = "right" )

framebaixo = tk.Frame(root)
framebaixo.pack(side = "bottom")

scrollup = tk.Button(frameesq, text="Scroll Up", command=s.scrollup)
scrollup.pack()

scrolldown = tk.Button(framedir, text="Scroll Down", command=s.scrolldown)
scrolldown.pack()

fastscrollup = tk.Button(frameesq, text="Fast Scroll Up", command=s.fastscrollup)
fastscrollup.pack()

fastscrolldown = tk.Button(framedir, text="Fast Scroll Down", command=s.fastscrolldown)
fastscrolldown.pack()

tlir = tk.Tk()
tlir.title("Loop Running..")
stop = tk.Button(tlir, text="STOP", command=s.stop)
stop.pack()
tlir.mainloop()

root.mainloop()

###################################################

