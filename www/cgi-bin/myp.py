#!/usr/bin/python36
import cgi
import subprocess
print("Content-type: text/html")
print()
subprocess.getoutput("yum install httpd")
subprocess.getoutput("systemctl restart httpd")
subprocess.getoutput("systemctl enable httpd")
print("Installed")
