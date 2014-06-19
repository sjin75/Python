#!/usr/bin/env python

src = input('Source Encoding (1: UTF-8, 2:EUC-KR): ')
term = input('Terminal Encoding (1: UTF-8, 2:EUC-KR): ')

if src == 1: # from utf-8
    # utf-8: '%' -> '\\x'
    str = raw_input('UTF-8 String in URL (with %\'s): ').replace('%','\\x').decode("string-escape")
    if term == 1:
        # to utf-8
        print str
    elif term == 2:
        # to euc-kr
        print str.decode('utf-8').encode('euc-kr')
    else: 
        print 'Invalid Terminal!'
        
elif src == 2: # from euc-kr
    # euc-kr: '%' -> '\\x'
    str = raw_input('Euc-kr String (with %\'s): ').replace('%','\\x').decode("string-escape")
    if term == 1:
        # to utf-8
        print str.decode('euc-kr').encode('utf-8')
    elif term == 2:
        # to euc-kr
        print str
    else: 
        print 'Invalid Terminal!'
else:
    print 'Invalid Input!'
