import welcome
import os
import sys
import getpass
import librarian
super_id="pes"      #set the super user id
super_pass="bsc"    #set the super user password
def sup_log():
    log=input("\nLogin ID:\n")
    password=getpass.getpass()
    if not(log==super_id and password==super_pass):
        print("\nInvalid super user ID or password\n")
        sup_a=input("1.Retry\nAny other key to go back")
        if sup_a=='1':
            os.system('cls')
            welcome.func()
            sup_log()
        else:
            os.system('cls')
            main()
    else:
        librarian.main2()

def lib_log():
    log=input("\nMemeber ID:\n")
    password=getpass.getpass()
    f=open("C:/Users/Administrator/Documents/Python Scripts/Library/librarians.txt")
    g=0
    while True:
        a=f.readline()
        if(len(a)==0):
            break
        mem=eval(a)
        if (mem[0]==log and mem[1]==password):
            g=1
            break
    if g==0:
        print("\nInvalid  user ID or Password\n")
        sup_a=input("\n1.Retry\nAny other key to go back")
        if sup_a=='1':
            os.system('cls')
            welcome.func()
            lib_log()
        else:
            os.system('cls')
            main()
    else:
        librarian.main1()
def main():
    welcome.func()
    print("\nLogin")
    print("\n1.Head Librarian")
    print("\n2.Librarian")
    print("\n3.Exit")
    a=input("\nEnter the Option\n")
    if a not in ['1','2','3']:
        print ("Wrong input")
        os.system('cls')
        main()
    elif a=='3':
        sys.exit()    #call the exit function
    elif a=='1':
        sup_log()
    elif a=='2':
        lib_log()
main()