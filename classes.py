import os
import json
class upm():
    def __init__(self, ext):
        self.ext = ext
    def createpwd(self):
        print("Now we will teach you to start create password wizard")
        web = input("First,what is the website for the password?(likes 'www.google.com'): ")
        usr = input("Next, what is the user for the password?(likes 'John'): ")
        pwd = input("Then, what is the password?(likes 'qwertyuiop'): ")
        name = input("Then, what is the name for the password?(likes 'Business-Email')(Space it not vaild!): ")
        instruction = input("Then, what is the password mean?(likes 'This password is for my business email'): ")
        psk = []
        psk.append(web)
        psk.append(usr)
        psk.append(pwd)
        psk.append(name)
        psk.append(instruction)
        fname = name + ".json"
        with open(fname, 'w') as f_obj:
            json.dump(psk, f_obj)
        print("Data saved!")
    def deletepwd(self):
        delpwd = input("Which password do you want to delete?(Name for password): ")
        print("Deleting...")
        os.system("del " + delpwd + "*")
        print("Data saved!")
    def license(self):
        print("License by orwtmc")
        print("Professional Version")
        print("Product key: 00000-00000-00000-00000-00000")
        print("Development Version")
        print("Microsoft Windows license")
        print("Registed by rsow001@gmail.com")
        print("Open Source software")
    def readpwd(self):
        print("Your password file extension must same as the view password's file extension")
        print("If they are different, we will can't found this file!")
        pwdnm = input("Password Name: ")
        fname = pwdnm + ".json"
        try:
            with open(fname) as f_obj:
                psk = json.load(f_obj)
        except FileNotFoundError:
            print("Something went wrong, please check everything is fine.")
        print("Website: " + psk[0])
        print("Username: " + psk[1])
        print("Password: " + psk[2])
        print("Instruction: " + psk[3])
        print("\n")
        print("Data saved.")
    def arcpwd(self):
        print("Must enter a password for archive!")
        arcpass = input("Archive password: ")
        print("Must enter the archive name!")
        arcname = input("Archive name: ")
        print("Encrypting...")
        os.system("7za.exe a " + arcname + ".zip " + "*.json -p" + arcpass)
        print("Deleting origin file...")
        os.system("del *.json")
        os.system("cls")
        print("Data saved!")
    def extpwd(self):
        arcname = input("Archive Name: ")
        arcpwd = input("Archive Password: ")
        print("Extracting...")
        os.system("7za.exe e " + arcname + ".zip -p" + arcpwd)
        print("Data saved")
    def delarc():
        arcname = input("Archive Name: ")
        print("Deleting Archive...")
        os.system("del " + arcname + ".zip")
