# This code translates text input from user into pig latin
# Import libraries

import numpy as np
import pandas as pd

# Take the users input
words = raw_input("Enter some text to check: ")

# Break apart the words into a list0

words_list = words.split(' ')
for word in words_list:
    if len(word) >= 3:

        pig_latin = word + "%say" % (word[0])
        pig_latin = pig_latin[1:]
        print(pig_latin)
    else:
        pass
