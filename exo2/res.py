import re

file = open("exo2.txt", "r")

regx = re.search('([ée].*\n)', file.read())
reg = re.findall('([ée])*', file.read())
print (regx)
file.close()

