import os
import json
#functions
while True:
    def createpwd():
        print("Now we will teach you to start create password wizard")
        web = input("First,what is the website for the password?(likes 'www.google.com'): ")
        usr = input("Next, what is the user for the password?(likes 'John'): ")
        pwd = input("Then, what is the password?(likes 'qwertyuiop'): ")
        name = input("Then, what is the remark for the password?(likes 'Business-Email')(Space it not vaild!): ")
        instruction = input("Then, what is the password mean?(likes 'This password is for my business email'): ")
        webfile = name + "-" + "web"
        usrfile = name + "-" + "usr"
        pwdfile = name + "-" + "pwd"
        insfile = name + "-" + "ins"
        print("Finally!We are saving data to your local disk!!!")
        with open(webfile, 'w') as f_obj:
            json.dump(web,f_obj)
        with open(usrfile, 'w') as f_obj:
            json.dump(usr,f_obj)
        with open(pwdfile, 'w') as f_obj:
            json.dump(pwd,f_obj)
        with open(insfile, 'w') as f_obj:
            json.dump(instruction,f_obj)
        try:
            os.system("ren " + name + "* " + name + "*." + fileext)
        except NameError:
            pass
        print("Data saved!")
    def deletepwd():
        delpwd = input("Which password do you want to delete?(Name for password): ")
        print("Deleting...")
        os.system("del " + delpwd + "*")
        print("Data saved!")
    def extension():
        try:
            print("Now file extension: " + fileext)
        except NameError:
            print("ext.ini does not exist, view operation is canceled!")
        ext = input("The file extension is: ")
        with open(fileextension, 'w') as f_obj:
            f_obj.write(ext)
        print("Data saved!")
    def license():
        print("License by orwtmc")
        print("Professional Version")
        print("Product key: 00000-00000-00000-00000-00000")
        print("Development Version")
        print("Microsoft Windows license")
        print("Registed by rsow001@gmail.com")
        print("Open Source software")
    def readpwd():
        print("Your password file extension must same as the view password's file extension")
        print("If they are different, we will can't found this file!")
        pwdnm = input("Password Name(NO extension): ")
        try:
            print("Reading Password...")
            pwdname = pwdnm
            usr = pwdnm + "-" + "usr." + fileext
            usr = usr.strip()
            pwd = pwdnm + "-" + "pwd." + fileext
            pwd = pwd.strip()
            web = pwdnm + "-" + "web." + fileext
            web = web.strip()
            ins = pwdnm + "-" + "ins." + fileext
            ins = ins.strip()
            with open(usr, 'r') as f_obj:
                usr_print = f_obj.read()
            with open(pwd, 'r') as f_obj:
                pwd_print = f_obj.read()
            with open(web, 'r') as f_obj:
                web_print = f_obj.read()
            with open(ins, 'r') as f_obj:
                ins_print = f_obj.read()
            print("Username: " + usr_print)
            print("Password: " + pwd_print)
            print("Website: " + web_print)
            print("Instruction: " + ins_print)
        except FileNotFoundError:
            print("The Required file could not be found!")
            print("Please check your destination file's extension is same than program's default file's extension")
    def arcpwd():
        print("We only archive the file extension = json!!!")
        print("Must enter a password for archive!")
        arcpass = input("Archive password: ")
        print("Must enter the archive name!")
        arcname = input("Archive name(no extension): ")
        print("Encrypting...")
        os.system("7za.exe a " + arcname + ".zip " + "*.json -p" + arcpass)
        print("Deleting origin file...")
        os.system("del *.json")
        os.system("cls")
        print("Data saved!")
    def extpwd():
        arcname = input("Archive Name(no extension): ")
        arcpwd = input("Archive Password: ")
        print("Extracting...")
        os.system("7za.exe e " + arcname + ".zip -p" + arcpwd)
        print("Data saved")
    def delarc():
        arcname = input("Archive Name(no extension): ")
        print("Deleting Archive...")
        os.system("del " + arcname + ".zip")
    #main program
    print("Welcome to Password Manager!")
    print("You are using upm-1.0")
    print("Only available on Microsoft Windows")
    print("Login at root@localhost")
    print("You want to..")
    print("1, Create a password")
    print("2, Delete a password")
    print("3, Change file extension")
    try:
        fileextension = "ext.ini"
        with open(fileextension, 'r') as f_obj:
            fileext = f_obj.read()
    except FileNotFoundError:
        os.system("echo json >> ext.ini")
    print("4, Program license")
    print("5, Read Memoried Password")
    print("6, Quit")
    print("7, Archive All Password")
    print("8, Extract Archived Password")
    print("9, Delete Archived Password")
    opt = input(">>> ")
    if opt == "1":
        createpwd()
    else:
        pass
    if opt == "2":
        deletepwd()
    else:
        pass
    if opt == "3":
        extension()
    else:
        pass
    if opt == "4":
        license()
    else:
        pass
    if opt == "5":
        readpwd()
    else:
        pass
    if opt == "6":
        break
    else:
        pass
    if opt == "7":
        arcpwd()
    else:
        pass
    if opt == "8":
        extpwd()
    else:
        pass
    if opt == "9":
        delarc()
    else:
        pass
