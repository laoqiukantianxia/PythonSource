import sys 
import re

def mac1(addr):
    '''
    Validates a mac address
    '''
    valid = re.compile(r'''
                      (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$)
                      ''',
                      re.VERBOSE | re.IGNORECASE)
    return valid.match(addr) is not None

def mac2(mac):
	if not ((len(mac) == 17 and not re.match('\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}', mac)) or \
                        (len(mac) == 12 and not mac.isalnum()) or len(mac) not in (12, 17)):
		print("True")
	else:
		print("False")


mac2(sys.argv[1])
