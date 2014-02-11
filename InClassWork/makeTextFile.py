#!/usr/bin/env pytho

'makeTextFile.py -- create text file'

import os

ls = os.linesep    # why?

# get filename
fname = raw_input('Enter file name ')

#if os.path.exists(fname):
#    print "ERROR: '%s' already exists" % fname

### Exercise 1
try:
    os.path.exists(fname)
except IOError, e:
    print "ERROR: '%s' already exists: " % fname, e
###
else:
    # get file content (text) line
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
    # loop until user terminates input
    while True:
        entry = raw_input('> ')
	    if entry == '.':
            break
        else:
            all.append(entry)

    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()

    print 'DONE!'
    
