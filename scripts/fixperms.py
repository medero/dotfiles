#!/usr/bin/python

from subprocess import call, Popen
import os, sys

total = len( sys.argv )

if total == 2:
    directory = str(sys.argv[1])

    print directory

    if os.path.exists(directory):
        try:
            call(['chown', '-R', 'root:web', directory])
            call(['chmod', '2775', directory ])
            call(['find', directory, '-type', 'd', '-exec', 'chmod', '2775', '{}', '+'])
            call(['find', directory, '-type', 'f', '-exec', 'chmod', '0664', '{}', '+'])
            print 'Fixed permissions in ' + directory
        except:
            print 'Failed to fix permissions'
