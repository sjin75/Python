#!/usr/bin/env python

import urllib.parse

str = urllib.parse.unquote(input('URL Encoded String (with %\'s): '))
print(str)
