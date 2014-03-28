'''
Created on Mar 19, 2014

@author: josh23941
'''

import iptools

def inc_ip (ip):
    return iptools.ipv4.ip2long(ip) + 1

def load_input(filename):
    try:
        with open(filename) as input_file:
            config = input_file.read()
            return config
    except IOError:
        print "Input file does not exist"

'''
def load_input(filename):
    try:
        with open(filename) as input_file:
            inputs = input_file.read().splitlines()
            for i in inputs:
                print "Loaded Input: " + i
            print
            return inputs
    except IOError:
        print "Input file does not exist"
'''