#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")
print()

#mydata=cgi.FieldStorage()
#r=mydata.getvalue('u')

x,y=subprocess.getstatusoutput("sudo ansible-playbook hadoopnamenode.yml")
'''print(x)
print(y)
if x==0:
	print("datanode created successfully")
else:
	print("sorry datanode not created")
print("\n")
print()
print(y)
'''
