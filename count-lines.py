""" This script counts the number of lines in a std input
Input: strings from the syste's std inputs
"""

import sys 			


count = 0
for line in sys.stdin:
	count += 1

print(count, 'lines in standard input')

