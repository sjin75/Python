#!/usr/bin/python
import os

for i in range(51,66,1):
    os.rename('kc-v9-n2-' + str(i) + '.indd', 'kc-v9-n2-' + str(i-1) + '.indd')
    print 'kc-v9-n2-' + str(i) + '.indd' + ' to ' + 'kc-v9-n2-' + str(i-1) + '.indd'

