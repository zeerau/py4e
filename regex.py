import re

# variable_one = 'My 2 favorite numbers are 19 and 42'
# regex1 = re.findall('[0-9]+',variable_one)
# print(regex1)

# regex2 = re.findall('[AEIOU]+', variable_one)
# print(regex2)

#string parsing
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

#double split pattern