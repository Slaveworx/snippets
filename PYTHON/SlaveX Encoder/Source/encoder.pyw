import base64 as b64 #Base64 Lib for encoding and decoding strings
import Tkinter as tk #graphical interface
import ttk #graphical interface templates and new styles
import tkMessageBox #loads imgbox
from sys import platform as _platform #will check the OS

class Buttons():
	global lbl
	
	def encode(self):
		get = tk.Entry.get(entry)
		en1 = b64.b32encode(b64.b64encode(get))
		self.lbl = tk.Entry(frmresult)
		self.lbl.insert(0, en1)
		self.lbl.grid(row=2)
		return en1
		
	def decode(self):
		get = tk.Entry.get(entry)
		de1 = b64.b32decode(get)
		final = b64.b64decode(de1)
		self.lbl = tk.Entry(frmresult)
		self.lbl.insert(0, final)
		self.lbl.grid(row=2)
		return final
		
	def about(self):
	   tkMessageBox.showinfo("CREDITS", "This encoder/decoder was created by Slaveworx! 2015 - doit@slaveworx.esy.es")
	   
	def reset(self):
		entry.delete(0,tk.END)
		self.lbl.delete(0,tk.END)


#####################

b = Buttons()	

#####################

#starting the window 
main = tk.Tk() #main window creation
main.title("Encoder & Decoder") #window title
main.resizable(0,0) #avoids resizing


#GETTING THE OPERATING SYSTEM IN ORDER TO USE THE RIGHT FAVICON
if _platform == "linux" or _platform == "linux2":
	main.iconbitmap("@img/icon.xbm")
elif _platform == "win32":
	main.iconbitmap("/img/icon.ico")

#FRAMES
frmlogo = tk.Frame() # LOGO FRAME
frmlogo.grid(row=0)  #

frmentry = tk.Frame() # TEXT ENTRY FRAME
frmentry.grid(row=1)  #

frmbtn = tk.Frame() # BUTTONS FRAME
frmbtn.grid(row=2)  #

frmresult = tk.Frame() # OUTPUT FRAME
frmresult.grid(row=3)  #

##########################################

#LOGO
img = tk.PhotoImage(file="img/logo.gif")
logo = tk.Label(frmlogo, image=img)
logo.grid()

#BUTTON ENCODE	
btn1 = ttk.Button(frmbtn, text="Encode!", command=b.encode)
btn1.grid(row=1,column=1)

#BUTTON DECODE	
btn2 = ttk.Button(frmbtn, text="Decode!", command=b.decode)
btn2.grid(row=1,column=2)

#BUTTON RESET
btn1 = ttk.Button(frmbtn, text="RESET", command=b.reset)
btn1.grid(row=2,column=1)

#BUTTON ABOUT
btn1 = ttk.Button(frmbtn, text="About", command=b.about)
btn1.grid(row=2,column=2)

#TXT ENTRY
global entry
entry = tk.Entry(frmentry)
entry.grid(row=0, column=1)


#MAINLOOP
main.mainloop()
