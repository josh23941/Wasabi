'''
Created on Mar 20, 2014

@author: josh23941
'''
import sys
import util
import request

if __name__ == '__main__':
    if len(sys.argv) > 0:
        inputs = util.load_inputs(sys.argv[1])
        for i in inputs:
            request.request_url(i)
    else:
        print "No input file specified."
        