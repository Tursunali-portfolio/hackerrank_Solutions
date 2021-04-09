```<js>
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    sentence = sentence.swapcase()  #this swaps case of string.
    sentence = sentence.split() #this converts string into a list
    sentence.reverse() #this reverses order of elemtents in list
    result = ""
    
    result = " ".join(sentence) #this makes up a string from list.
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()

```
