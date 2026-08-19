

import re

# Search for an exact string match
if re.search("ape", "The ape was at the apex"):     #search - true/false return kore
	print("There is an ape")

# findall() returns a list of matches and . is used to match any 1 character or space
all_apes = re.findall("ape.", "The ape was at the apex")
print(all_apes)

txt = "The rain in Spain"
x = re.split("\s", txt)                 # \s mean space dibe
print(x)
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "-", txt)
print(x)


