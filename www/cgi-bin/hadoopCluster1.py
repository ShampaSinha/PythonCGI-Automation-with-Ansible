#!/usr/bin/python36
import subprocess
import cgi

print("content-type: text/html")
print()

a,b=subprocess.getstatusoutput("sudo ansible-playbook hadoopdatanode.yml")
'''if a==0:
        print("namenode created successfully")
else:
        print("sorry namenode not created")
print("\n")
print()
print(b)
'''
