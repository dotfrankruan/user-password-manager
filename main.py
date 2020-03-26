import os
import json
from classes import *
#main program
print("Welcome to Password Manager!")
print("You are using upm-1.1")
print("Logged in: root@localhost")
print("You want to..")
print("1, Create a password")
print("2, Delete a password")
try:
   fileextension = "ext.ini"
   with open(fileextension, 'r') as f_obj:
       fileext = f_obj.read()
except FileNotFoundError:
        os.system("echo json >> ext.ini")
print("3, Program license")
print("4, Read a Password")
print("5, Quit")
print("6, Archive All Password")
print("7, Extract Archived Password")
print("8, Delete Archived Password")
#functions
while True:
    opt = input(">>> ")
    if opt == "1":
        upm.createpwd(fileext)
    else:
        pass
    if opt == "2":
        upm.deletepwd(fileext)
    else:
        pass
    if opt == "3":
        upm.license(fileext)
    else:
        pass
    if opt == "4":
        upm.readpwd(fileext)
    else:
        pass
    if opt == "5":
        break
    else:
        pass
    if opt == "6":
        upm.arcpwd(fileext)
    else:
        pass
    if opt == "7":
        upm.extpwd(fileext)
    else:
        pass
    if opt == "8":
        upm.delarc(fileext)
    else:
        pass
