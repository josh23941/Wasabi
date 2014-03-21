'''
Created on Mar 20, 2014

@author: josh23941
'''
import sys
import util

if __name__ == '__main__':
    if len(sys.argv) > 0:
        util.load_inputs(sys.argv[1])
    else:
        print "No input file specified."
        