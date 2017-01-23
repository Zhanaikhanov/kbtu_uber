#!/usr/bin/env python3
import cgi, html

form = cgi.FieldStorage()
text1 = html.escape(form.getfirst('NAME'))
text2 = html.escape(form.getfirst('SURNAME'))
print("Set-Cookie: name={}".format(text1))
print("Content-type: text/html")
print()

print("""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Start page!</title>
</head>
<body>""")
print( '<h1>Hello ! {} </h1>'.format(text1)) 
print("""<p>This is {} first start page!</p>
	<form action='/cgi-bin/form1.py'>
		<input type='chekbox' name='like' value='yes'>Do you like it?<br/>>
		<input type='submit'>
	</form>
</body>
</html>""".format(text2))