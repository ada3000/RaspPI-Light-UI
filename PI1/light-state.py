#!/usr/bin/python
import cgi
import os

stateFile = "/home/pi/LightDaemon/worker.state"

print "Content-Type: text/html\n"

f = open(stateFile,"r")		
line = f.readline()
f.close()

print line		

#print  os.popen(stateFile).read()
#b = {}
#b["aa"]="bbb"
#a[0]=100
#print a.append(100000)
#print a
#print a[5]
#print len(a)
#print b["aa"]
#c="sss"
#print "OK {0} OK".format(c)


#print os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()