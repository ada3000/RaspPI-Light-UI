#!/usr/bin/python
import cgi
import os

commandFile = "/prod/worker.command"

print "Content-Type: text/html\n"

print "start"

params = cgi.FieldStorage()
cmd = params["cmd"].value

f = open(commandFile,"w")		
f.write(cmd)
f.close()

print "{state:\"success\"}"
