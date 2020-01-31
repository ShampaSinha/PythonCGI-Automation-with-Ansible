#!/usr/bin/python36
import subprocess
import cgi

print("content-type: text/html")
print()

form=cgi.FieldStorage()
docker_name=form.getvalue('n')
docker_ime=form.getvalue('img')
c=subprocess.getoutput("sudo docker run -it -d --name {} {}".format(docker_name,docker_ime))
print(c)
