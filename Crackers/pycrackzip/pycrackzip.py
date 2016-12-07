#!/usr/bin/python
# -*- coding: utf-8 -*-
# By: E4404_404
# pogTeam
# Date: 07/12/2016

# https://docs.python.org/2/library/zipfile.html?highlight=zipfile#module-zipfile
import zipfile
# https://docs.python.org/2/library/optparse.html?highlight=optparse#module-optparse
# https://docs.python.org/2/library/argparse.html#module-argparse
import optparse
# https://docs.python.org/2/library/threading.html
from threading import *
# https://pypi.python.org/pypi/termcolor
from termcolor import colored

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password: ' + password + '\n'
    except:
        pass

def main():
    parser = optparse.OptionParser("usage: ./pyzip.py " + "-f file.zip -d wordlist")
    parser.add_option('-f', dest='zname', type='string',help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',help='specify dictionary file')

    (options, args) = parser.parse_args()

    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        zFile = zipfile.ZipFile(zname)
        passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Check pyzip interrupted by user, killing..!!"
