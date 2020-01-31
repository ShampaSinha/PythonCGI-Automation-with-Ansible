#!/usr/bin/python36
print('content-type:text/html')
print()

import cgi
webdata = cgi.FieldStorage()
name = webdata.getvalue('name')
uid = webdata.getvalue('name')
gid = webdata.getvalue('name')
comment = webdata.getvalue('name')
home = webdata.getvalue('name')
shell = webdata.getvalue('name')


print(webdata)
