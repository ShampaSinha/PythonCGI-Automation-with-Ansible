#!/usr/bin/python36
print("content-type: text/html")
print()

import subprocess as sp
x=sp.getoutput("ansible playbook photo.yml")
print(x)
