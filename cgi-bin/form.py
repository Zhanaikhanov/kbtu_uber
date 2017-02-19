#!/usr/bin/env python3
import cgi , html

sign_in = open('index.html','r').read()
reg_in = open('registering_uber.html','r').read()
error_reg_in = open('error_register.html','r').read()
main = open('main.html','r').read()
after_main = open('after_main.html','r').read()
choose = open('choose.html','r').read()

form = cgi.FieldStorage()
users = [{"beka": "123"}]

uname = form.getfirst("username")
password = form.getfirst('password')
uname = str(html.escape(uname) )
passw = str(html.escape(password) )

print("Content-type: text/html")
print()

for user in users:	
	if uname in user:
		if passw == str(user[uname]):
			print(choose.format(uname))
			break 
		else:
			print(sign_in.format("",''))
			break
	else:
		print(sign_in.format('',''))
		break
