#!/bin/python

__author__ = 'root'

import sys
import commands

def changePass (username , password) :
    shadow = open("/etc/shadow" , "r")
    if shadow :
        lines = shadow.readlines()
        shadow.close()
        for line in lines :
            if line.find(username) == 0 :
                tempLine = line
                lines.remove(line)
                tempLine = tempLine.split(":")
                tempLine[1] = commands.getoutput("python -c 'import crypt; print crypt.crypt(\"%s\", \"$6$AWI-CO$\")'" %(password))
                lines.append(str.join(":",tempLine))
        shadow = open("/etc/shadow" , "w")
        shadow.write(str.join("",lines))
        shadow.close()

    else :
        print "file '/etc/shadow' is not open !"


if __name__ == "__main__" :
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-u')
    parser.add_argument("-p")
    args = parser.parse_args()
    try :
        username = args.u
        password = args.p
    except :
        print "bad argument passed !"
        exit ()
    if (username == None or password==None) :
        print "bad argument passed !"
        exit ()
    changePass(username , password)