#!/usr/bin/python36
import subprocess
import cgi
print("context-type: text/html")
print()
var=cgi.FieldStorage()
a=var.getvalue("n")
b=var.getvalue("p")
x=subprocess.getoutput("sudo useradd {}".format(a))
print(x)
y=subprocess.getoutput('id {}'.format(a))
print(y)
z1=subprocess.getstatusoutput("echo '{}' | sudo passwd {} --stdin".format(b,a))
if(z1[0]==0):
	print("It worked:\n")
else:
	print("GOT")
