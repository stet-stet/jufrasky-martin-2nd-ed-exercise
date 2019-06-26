# Write regular expressions for the following languages.
# We are gonna use python
# By "word", we mean an alphabetic string separated from other words 
# by whitespace, any relevant punctuation, line breaks, and so forth.

import re

# quick notes:
# \b: stands for boundary
# \d: stands for digit
# \s: stands for space
# \w: stands for word

# 1. the set of all alphabetic strings.

crit1 = re.compile('[a-zA-Z]+') 
# can we like....get a union of \w and \D ?

# 2. the set of all lower case alphabetic strings ending in a b
crit2 = re.compile('[a-z]*b')

# 3. the set of all strings with two consecutive repeated words (eg. Humbert Humbert)
# withour the r, we would need FOUR \s, two for strings, one for regex.
crit3 = re.compile(r'\b([a-zA-Z]+)[.,\?\!]?\s\1\b')

# 4. the set of all strings from the alphabet a,b such that 
# each a is immediately preceded by and immediately followed by a b
crit4 = re.compile(r'^(b|(bab))*$')
# this works. 
print(crit4.match('baab'))
print(crit4.match('bbab'))
print(crit4.match('babb'))

# 5. all string sthat start at the beginning of the line with an integer 
# and that end at the EOL with a word
crit5 = re.compile(r'^\d.*\s[a-zA-Z]+$')

# 6. all strings that have both the word grotto and the word raven in them
crit6 = re.compile(r'(.*\sgrotto.*\sraven.*)|(.*\sraven.*\sgrotto.*)')

# 7. write a pattern that places the first word of an English sentence in a register. 
# Deal with punctuation.
crit7 = re.compile(r'^([a-zA-Z]+).*')
b = input("Write your sentence: ")
if crit7.match(b):
    print(crit7.match(b).group(1))
else:
    print("we failed.")
