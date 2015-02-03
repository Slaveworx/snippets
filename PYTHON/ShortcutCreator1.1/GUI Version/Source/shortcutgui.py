#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################################
#                    SHORTCUT CREATOR FOR LUBUNTU    v1.2             #
#         Copyright 2015 - Tiago Galvão - doit@slaveworx.esy.es       #
#######################################################################

#####################################################################
from Tkinter import *											    #
import Tkinter as tk     				                            #
import ttk														 	#
import tkMessageBox													#
import tkFileDialog													#
import os, sys, stat											    #
#####################################################################

""" This class defines the functions for the buttons we are going to
use in Lubuntu Shortcut Creator 1.2. Any doubt please report to:
doit@slaveworx.esy.es"""

class Btnfuncs():
	global shortcut, filename, version, v, com, name, iconpath
	
	
	def openfile(self):
		self.iconpath = tkFileDialog.askopenfilename()
		return self.iconpath
		
		
	def create(self):
		
		#this if statement will make error handling
		
		if len(tk.Entry.get(filename and version and com and name)) > 0 and (v.get() == "true" or v.get() == "false"):	
			shortcut = open(tk.Entry.get(filename) + ".desktop", "a+")
			shortcut.write("[Desktop Entry]\nEncoding=UTF-8\n");
			shortcut.write("Version=" + tk.Entry.get(version) + "\n");
			shortcut.write("Type=Application" + "\n");
			shortcut.write("Terminal=" + v.get() + "\n");
			shortcut.write("Exec=" + tk.Entry.get(com) + "\n");
			shortcut.write("Name=" + tk.Entry.get(name) + "\n");
			
			#will handle the icon path
			shortcut.write("Icon=" + str(self.iconpath) + "\n");
			
			#will handle chmod to make the shortcut executable
			final = tk.Entry.get(filename) + ".desktop"
			os.chmod(final, stat.S_IRWXU)
			tkMessageBox.showinfo("Shortcut Created!", "Shortcut was created successfuly!")
			self.reset()
		else:
			tkMessageBox.showerror("Error!", "Please fill all the parameters!")	
		
		
	def reset(self):
		filename.delete(0,tk.END)
		version.delete(0,tk.END)
		com.delete(0,tk.END)
		name.delete(0,tk.END)
		
	
	def about(self):
	   tkMessageBox.showinfo("CREDITS", "This software was created by Slaveworx! 2015 - doit@slaveworx.esy.es")
	   
	def closewindow(self):
		main.destroy()

#####################################################################
"""This script is the graphical version of the Lubuntu Shortcut 
Creator 1.1 that I've made before just on console mode. Any doubt
or suggestion can be sent to doit@slaveworx.esy.es. Thank you!!"""

#####################################################################

#MAIN WINDOW DEFINITIONS
main = tk.Tk()
main.title("Lubuntu Shortcut Screator 1.2")
main.resizable(0,0)
b = Btnfuncs()

#FRAMES
frmtitle = tk.Frame(main)
frmtitle.grid(row=0)

frmbody = tk.Frame(main)
frmbody.grid(row=1)

frmradio = tk.Frame(frmbody)
frmradio.grid(row=2)

frmbuttons = tk.Frame(main)
frmbuttons.grid(row=3)

#BUTTONS
btn1 = ttk.Button(frmbuttons, text="Create", command=b.create)
btn1.grid(row=0,column=0)

btn2 = ttk.Button(frmbuttons, text="Reset", command=b.reset)
btn2.grid(row=0,column=1)

btn3 = ttk.Button(frmbuttons, text="Close", command=b.closewindow)
btn3.grid(row=0,column=2)

btn4 = ttk.Button(frmbuttons, text="About", command=b.about)
btn4.grid(row=0,column=3)

#LOGO
img = tk.PhotoImage(file="img/logo.gif")

#LABELS

lbl0 = tk.Label(frmtitle, text="Lubuntu Shortcut Creator 1.2", image=img)
lbl0.grid(row=0,column=0)

lbl1 = tk.Label(frmbody, text="*Filename:")
lbl1.grid(row=0,column=0)

lbl2 = tk.Label(frmbody, text="*Version:")
lbl2.grid(row=1,column=0)

lbl3 = tk.Label(frmradio, text="*Execute in Terminal:")
lbl3.pack()

lbl4 = tk.Label(frmbody, text="*Command:")
lbl4.grid(row=3,column=0)

lbl5 = tk.Label(frmbody, text="*Shortcut Name:")
lbl5.grid(row=4,column=0)

lbl6 = tk.Label(frmbody, text="*Icon Path:")
lbl6.grid(row=5,column=0)

lbl7 = tk.Label(frmbody, text="*All fields are compulsory!", fg="#E70303")
lbl7.grid(row=7,column=0)

#ENTRIES

filename = ttk.Entry(frmbody)
filename.grid(row=0,column=1)

version = ttk.Entry(frmbody)
version.grid(row=1,column=1)

com = ttk.Entry(frmbody)
com.grid(row=3,column=1)

name = ttk.Entry(frmbody)
name.grid(row=4,column=1)

icon = ttk.Button(frmbody, text="Choose Icon ...", command=b.openfile)
icon.grid(row=5, column=1)

#RADIO BUTTONS

v = StringVar()
yes = tk.Radiobutton(frmradio, text="Yes", variable=v, value = "true")
yes.pack(side="left")
no = tk.Radiobutton(frmradio, text="No", variable=v, value = "false")
no.pack()

tk.Radiobutton.select(yes)


#MAINLOOP
main.mainloop()
