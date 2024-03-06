from inspect import modulesbyfile
from unittest import result


import re

filename = "./dumpfile.txt"
result_filename = "./result.txt"

inputfile  = open(filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')

lookfor = r"[\w.-]+@(?!outlook\.ca)[A-Za-z-]+\.[\w.]+"  # can check on the https://regex101.com/ 

mytext = inputfile.read()

results = re.findall(lookfor, mytext)



for item in results:
    print(item)
    resultfile.write(item + "\n") 


print("Total: " + str(len(results)))

