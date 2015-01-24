#!/usr/bin/env python
# -*- coding: utf-8 -*-
#######################################################################
#                    SHORTCUT CREATOR FOR LUBUNTU    v1.1             #
#         Copyright 2015 - Tiago Galvão - doit@slaveworx.esy.es       #
#######################################################################

print ("############### Lubuntu Shortcut Creator v1.0 ###############")
file_name = str(raw_input("#  Insert the desired filename > "))

shortcut = open(file_name + ".desktop", "a+")

shortcut.write("[Desktop Entry]\nEncoding=UTF-8\n");
print ("###############################################################\n")
version = str(raw_input("\nInsert the program version > "))

shortcut.write("Version=" + version + "\n");
shortcut.write("Type=Application" + "\n");

terminal = raw_input("Use terminal to launch? (True ou False)> ")
shortcut.write("Terminal=" + terminal + "\n");

command = str(raw_input("Insert the command to execute > "))
shortcut.write("Exec=" + command + "\n");

name = str(raw_input("Insert the shortcut name > "))
shortcut.write("Name=" + name + "\n");

print ("\nShortcut created successfully!!!\n\n")

print ("Created by Shortcut Creator 1.1")


shortcut.close()

