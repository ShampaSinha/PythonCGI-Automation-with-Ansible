#!/usr/bin/python36
import cgi
import subprocess
x=subprocess.getoutput("sudo docker images")
print("Content-type: text/html")
print()
print('<form action="http://192.168.56.107/cgi-bin/dock.py">')
print('Enter docker name<input box name="n" />')
print('<br/>')
print("Select image: ")
print("<select name='img'>")
for i in x.split("\n")[1:]:
	j=i.split() 
	print("<option>"+j[0]+":"+j[1]+"</option>")
print("</select>")
print('<br/>')
print('<input type="submit"'/)
print('</form>')

