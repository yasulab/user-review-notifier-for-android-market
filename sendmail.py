#!/usr/bin/env python
# -*- coding: utf-8 -*-

SENDMAIL = "/usr/sbin/sendmail" # sendmail location
import os

def read_file(filename):
    input = open(filename, "r")
    return input.read()
        
def sendmail(body, to_addr):
    p = os.popen("%s -t" % SENDMAIL, "w")
    p.write("To: "+to_addr+"\n")
    p.write("Subject: User Review Notifier for Android Market\n")
    p.write("\n") # blank line separating headers from body
    p.write(body)
    p.write("\n----- END -----\n")
    sts = p.close()
    if sts != 0:
        print "Sendmail exit status", sts


if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if argv_len == 3:
        filename = sys.argv[1].lower()
        to_addr = sys.argv[2].lower()
    else:
        print "USAGE: python sendmail.py FILENAME TO_ADDR"
        exit()
    body = read_file(filename)
    if body == "":
        print "There is nothing to send."
    else:
        sendmail(body, to_addr)

