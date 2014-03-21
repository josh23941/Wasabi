'''
Created on Mar 20, 2014

@author: josh23941
'''
import sys

if __name__ == '__main__':
    if len(sys.argv) > 0:
        try:
            with open(sys.argv[1]) as ti:
                inputs = ti.read().splitlines()
                print inputs
                for i in inputs:
                    print i
        except IOError:
            print "Input file does not exist"
    else:
        print "No input file specified."
        