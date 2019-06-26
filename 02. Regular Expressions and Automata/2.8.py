# write a regex for the language accepted by the NFSA in Fig 2.26

# the language accepted are of the form:
# the language on q1 is of the form: 
# a(ba|baa)*
# therefore the language on q1 is of the form:

import re
re.compile('a(ba|baa)*(b|ba)')
