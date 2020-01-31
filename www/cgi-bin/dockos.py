#!/usr/bin/python36
import subprocess
import cgi
print("content-type:text/html")
print()
cmd="sudo docker ps -a"
out=subprocess.getoutput(cmd)
con_list=out.split("\n")
print("<iframe width='100%' name='console'></iframe>")
print("""
<table border='5' width='100%'><tr>
<th>Container name</th><th>Image name</th>
<th>Status</th><th>Start</th>
<th>Stop</th><th>Terminate</th><th>console</th>
</tr>""")
for c in con_list[1:]:
	if "Up" in c :
		cstatus="running"
	elif "Exited" in c:
		cstatus="Stopped"
	else:
		cstatus="Unknown"
	a=c.split()
	b=a[-1]
	d=a[1]
	print("""<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.56.107/cgi-bin/dock1.py?s={}'>Stop</a></td>
	<td><a href='http://192.168.56.107/cgi-bin/dock2.py?s={}'>Start</a></td>
	<td><a href='http://192.168.56.107/cgi-bin/dock3.py?s={}'>Terminate</a></td>
	<td><a target='console' href='http://192.168.56.107:4200'>Console</a></td>
	</tr>""".format(b,d,cstatus,b,b,b))
print("</table>")



