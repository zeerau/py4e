# tuples

# tuples are immutable and ordered ,they can't be reaasigned like strings
# tupples are created using parenthesis and comma separated if many
# tuples doesn't has the following attributes:sort,append,reverse

# my_tuple = ('zarau', 'khadija','ukasha')
# print(my_tuple[1])

# tuples and dictionaries
#the items() methods in dictionaries returns a list of key and value tuples

# my_dict= dict()
# my_dict['name'] = 'basma'
# my_dict['age'] = 20

# for (key,value) in my_dict.items():
#     print(key,value)
# turn_tuple = my_dict.items()
# print(turn_tuple)

#tuples are comparable 
# comparison operators works with tuple, it iterate through sequeces until it find elements that differ


# print((2,5,7)<(4,6,9))
# print((0,1,200000)<(0,3,4))
# print(('mango', 'oranges')>('watermelon','apple'))


#sorting with tuples
# using the sorted method that takes a sequence as a parameter and return a sorted tuple
new_dict = {
    'breakfast':'egg',
    'lunch':'rice',
    'dinner': 'fruits'
}

sort_dict = sorted(new_dict.items())
print(sort_dict)