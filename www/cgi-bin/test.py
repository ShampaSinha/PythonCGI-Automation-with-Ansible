#!/usr/bin/python36
import subprocess
import cgi
print("context-type: text/html")
print()
cmd=subprocess.getoutput("sudo docker ps")
print(cmd)

