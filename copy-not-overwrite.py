# Copying from the Source Directory into the Target Directory
# No overwriting

#!/usr/bin/env python

import os
import shutil

source = input('Source Dir = ')
target = input('Target Dir = ')

list_target = os.listdir(target)

for name in os.listdir(source):
    if name not in list_target:
        print('Copying ' + name)
        shutil.copy2(source+'\\'+name, target)
