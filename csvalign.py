
#import string

def body(text):
    lines = text.split('\n')
    for line in lines: 
        words = line.split(',')
        for word in words:
                word = word.strip()
#                length = len(word.encode('utf-8'))
                word = word[:11]
                word = word.encode('euc-kr')
                length = len(word)
                if length < 22:
                        word += (b' ' * (22-length))
#                print('(' + str(length) + ')') 
                print(word.decode('euc-kr'), end='\t') 
        print('\n')

if __name__ == '__main__':
    import sys                             # when run, not imported
    body(open(sys.argv[1]).read())     # page contents of file on cmdline

