#!/usr/bin/python
import cgi
import os
import time

def getCoreTemp(id):
	return os.popen("cat /sys/class/thermal/thermal_zone{0}/temp".format(id)).read()
	
def getW1Temp(id):
	fileName = "cat /sys/bus/w1/devices/{0}/w1_slave".format(id)
	return os.popen(fileName).read().split("\n")[1].split("=")[1]

print "Content-Type: text/html\n"

config = {}

config["core0"] = {}
config["core0"]["param"]="0"
config["core0"]["type"]="core"

config["inner"] = {}
config["inner"]["param"]="28-0000066a9cc9"
config["inner"]["type"]="w1"

config["power"] = {}
config["power"]["param"]="28-000006261912"
config["power"]["type"]="w1"

config["room"] = {}
config["room"]["param"]="28-00000627e96e"
config["room"]["type"]="w1"

params = cgi.FieldStorage()

id = params["id"].value
item = config[id]
#print item

value=0
#print  os.popen("cat /sys/bus/w1/devices/28-0000066a9cc9/w1_slave").read().split("\n")[1].split("=")[1]
if (item["type"] == "core"):
	value = getCoreTemp(item["param"])
else:
	value = getW1Temp(item["param"])

timeValue = time.time();
#print value
print ("{{\"id\":\"{0}\",\"type\":\"{1}\",\"value\":{2},\"mesaure\":\"mC\",\"time\":{3}}}".format(id,item["type"],value,timeValue))