#!/usr/bin/python36
print("content-type: text/html")
print()


import cgi
import subprocess as sp
mydata=cgi.FieldStorage()

akey=mydata.getvalue("akey")
skey=mydata.getvalue("skey")



x=sp.getoutput("sudo ansible-playbook --extra-vars 'akey={}' --extra-vars 'skey={}' /root/ec2launch.yml".format(akey,skey))

#print(x)
