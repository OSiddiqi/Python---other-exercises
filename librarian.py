import search
import issueCopy
import returnCopy
import finalFineEval
import datetime
import getpass
import os
import collectFines
import reissueCopy
import addBook
import sys
import welcome
class lib:
    def search(self,x):
        searching.main(x)   
    def issue(self,x):
        issue_c.main(x)         
    def renew(self,x):
        reissue_c.main(x)
    def retrn(self,x):
        flag=0
        os.system('cls')
        welcome.func()
        bid=input("\nEnter the book ID to be returned\n")
        f=open("C:/Users/Administrator/Documents/Python Scripts/Library/books.txt")
        while True:
            w=f.readline()
            if(len(w)==0):
                break
            b=eval(w)
            if(b[0]==bid and b[8]!='#'):
                flag=1
                break
        if flag==0:
            print"\nEither this book doesn't exist in the library or this book has not been isssued to anyone\n"
            inp=input("\nPress 1 for typing the book ID again\nAny other key to go back")
            if(inp=='1'):
                self.retrn(x)
            else:
                if (x==1): 
                    os.system('cls')
                    main1()
                else:
                    os.system('cls')
                    main2()
        f.close()
        d1=datetime.date.today()
        returnCopy.main(bid,d1,x)
    def add(self,x):
        add_book.main(x)
    def exi(self):
        sys.exit()
class sup_lib(lib):  
    def addmem(self,x):
        y=0
        l=[]
        g=open("C:/Users/Administrator/Documents/Python Scripts/Library/librarians.txt")
        a=input("\nEnter the login ID please\n")
        while True:
            w=g.readline()
            if(len(w)==0):
                break
            d=eval(w)
            l.append(d)
            if d[0]==a:
                y=1           
        g.close()        
        if y==1:
            inp=input("\nThis login name already exists\nPress 1 to select a new login name\nAny other key to go back")
            if inp=='1':
                self.addmem(y)
            else:
                if (x==1):
                    os.system('cls')
                    main1()
                else:
                    os.system('cls')
                    main2()
        f=open("/Python27/libr/librarians.txt","w")
        print("\nLogin name is valid\nType a password\n")
        password=getpass.getpass()
        print("\n"+a+" has been added as a member of The Library\n")
        y=[a,password]
        l.append(y)
        f.write(str(l[0]))
        for i in l[1:]:
            f.write("\n"+str(i))
        f.close()
        inp=input("\nType 1 to enter another\nElse anything else to go back\n")
        if inp=='1':
            self.addmem(x)
        else:  
          # if (x==1):                   
         #      os.system('cls')
           #    main1()
           #else:
               os.system('cls')
               main2()
   
                   
    def gendue(self,x):
        final_fine_eval.main(x)
    def finecollect(self,x):
        final_collect_fine.main(x)       
def main1():
    x=1
    obj=lib()
    os.system('cls')
    welcome.func()
    print("\nWelcome Librarian ")
    a=input("\n\n1.Search for a book\n\n2.Issue a book\n\n3.Reissue a book\n\n4.Return a book\n\n5.Add a Book\n\n6.Exit\n")
    if a=='1':
        obj.search(x)
    elif a=='2':
        obj.issue(x)
    elif a=='3':
        obj.renew(x)
    elif a=='4':
        obj.retrn(x)
    elif a=='5':
        obj.add(x)
    elif a=='6':
        obj.exi()
    else:
        print "\nWrong Entry\n"
        main1()
def main2():
    x=2
    obj=sup_lib()
    os.system('cls')
    welcome.func()
    print("\nWelcome Librarian\n")
    a=input("\n1.Search for a book\n\n2.Issue a book\n\n3.Reissue a book\n\n4.Return a book\n\n5.ADD A NEW LIBRARIAN\n\n6.Generate the list of the students with due books\n\n7.Generate the list of students with fine\n\n8.Add a Book\n\n9.Exit\n")
    if a=='1':
        obj.search(x)
    elif a=='2':
        obj.issue(x)
    elif a=='3':
        obj.renew(x)
    elif a=='4':
        obj.retrn(x)
    elif a=='5':
        obj.addmem(x)
    elif a=='6':
        obj.gendue(x)
    elif a=='7':
        obj.finecollect(x)
    elif a=='8':
        obj.add(x)
    elif a=='9':
        obj.exi()
    else:
        print"\nWrong Entry\n"
        main2()