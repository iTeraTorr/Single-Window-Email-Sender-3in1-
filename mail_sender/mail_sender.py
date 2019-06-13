import smtplib
import webbrowser
import getpass
while True:
    temp=0
    email=input('enter your email address: ')
    if email[-4:]!='.com' or email.count("@")<=0:
        print("Please enter a valid email address: ")
        continue
    password=getpass.getpass("Kindly enter your Password: ")
    if email[-9]=='g':
        port='smtp.gmail.com'
    elif email[-9]=='y':
        port='smtp.mail.yahoo.com'
    elif email[-9]=='t':
        port='smtp-mail.outlook.com'
    else:
        print("We provide services for only gmail,yahoo and hotmail\n")
        continue
    print("Received your email and password...")
    while True:
        try:
            connection=smtplib.SMTP(port,587)
            connection.ehlo()
            connection.starttls()
            connection.login(email,password)
            temp=2
        except:
            if port=='smtp.gmail.com':
                print("Login unsuccessful, there are 2 possible reasons: ")
                print("1. You typed wrong username or password")
                print("2. You are using Gmail, there is an option in gmail 'allow less secure apps'")
                print("Do you want to open a webpage from where you can enable this option ?")
                ans=input("yes or no ? : ")
                if ans=="yes":
                    webbrowser.open("https://myaccount.google.com/lesssecureapps",new=2)
                    temp=1
                    break
                else:
                    print("Kindly consider retyping your email and password\n")
                    temp=1
                    break
        break
    if temp==1:
        continue
    else:
        break
receiver=input('Enter receiver\'s email address: ')
connection.sendmail(email,receiver,"Subject: "+input("Enter Subject : ")+"\n\n"+input("Enter Message : "))
connection.quit()