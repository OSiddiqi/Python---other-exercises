import librarian
import os
import sys
def main(x):
    lis=[]
    f=open("C:/Users/Administrator/Documents/Python Scripts/Library/books.txt","r")
    while True:
        l=f.readline()
        if (len(l)==0):
            break
        m=eval(l)
        lis.append(m)
        id=m[0]
    f.close()
    q=list(id)
    s1=q[5]
    s1=int(s1)
    s2=q[4]
    s2=int(s2)
    s3=q[3]
    s3=int(s3)
    s=s1+(10*s2)+(100*s3)
    s=s+1
    if(s<=9):
        q[5]=str(s)
    elif(s<=99):
        a=s%10
        q[5]=a
        s=s/10
        q[4]=s
    else:
        q[5]=s%10
        s=s/10
        q[4]=s%10
        s=s/10
        q[3]=s
    s1 = ''.join(str(n) for n in q)
    print s1
    n=0
    while (n==0):
        try:
            b_n=input("\nEnter book name\n")
            b_c=input("\nEnter category\n")
            b_a=input("\nEnter author\n")
            b_p=input("\nEnter price\n")
            b_e=input("\nEnter edition\n")
            b_y=input("\nEnter year\n")
            b_pu=input("\nEnter publisher\n")
            n=1
        except SyntaxError:
            print "Something went wrong"
            n=0
        except:
            print "Something went wrong"
            n=0
    l=[s1,b_n,b_c,b_a,b_p,b_e,b_y,b_pu,'#']
    lis.append(l)
    f.close()
    f=open("C:/Users/Administrator/Documents/Python Scripts/Library/books.txt","w")
    f.write(str(lis[0]))
    for i in lis[1:]:
        f.write("\n"+str(i))
    print("\nBook added Succesfully\n")
    f.close()
    a=input("\nTo Add another book press 1\nPress any key to go back\n")
    if a=='1':
        main(x)
    else:
        if (x==1):
            os.system('cls')
            librarian.main1()
        else:
            os.system('cls')
            librarian.main2()