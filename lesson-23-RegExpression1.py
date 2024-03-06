import re

mytext = "vasya aaaa 1972, Kolya -197222222: Olesya 1981, aaaaa@intel.com " \
         "bbbbbb@intel.com, Kolya -1972: Vlad 123, aaaaa@intel.com " \
         "ccccc@intel.com2, Kolya -1972: Maria #65, aaaaa@intel.com " \
         "sdsadxcb@intel.com, Kolya -1972: Alia 1981, aaaaa@intel.com " \
         "cadsadsadsa@intel.com, Kolya -1972: Lia 1981, #1231 " 

"""

\d  = Any digit 0-9
\D  = Any non digit
\w  = Any a;phabet symbol [A-Z a-z]
\W  = Any non Alphabet symbol
\s  = breakspace
\S  = non breakspace 

[0-9]{3}
[A-Z][a-z]+
\w

"""
textlookfor = r"@\w+\.\w+"
allresult = re.findall(textlookfor, mytext)

print(allresult)