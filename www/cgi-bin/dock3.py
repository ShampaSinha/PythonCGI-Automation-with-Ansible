mport subprocess
import cgi
print("content-type:text/html")
form=cgi.FieldStorage()
cname=form.getvalue("s")
cmd="sudo docker rm -f {}".format(cname)
x=subprocess.getoutput(cmd)
print("location:http://192.168.56.107/cgi-bin/dockos.py")
print()

