# Chapter 1

# Section 1.3
# Constructing a dictionary without excessive quoting

print()
print('APPROACH 1:\n')
# constructing simple dictionary (meant for small dictionaries)
# beginner friendly approach to understand mappings
print('BEGINNER FRIENDLY APPROACH TO UNDERSTAND MAPPINGS USING : {key:value}\n')
data = {'red' : 1, 'green' : 2, 'blue' : 3}
print('data using simple short concise default method: \n', data, '\n')
print('*****************************************************\n')


# Python collects the keyword arguments in a dictionary
def makedict(**kwargs):
    return kwargs
print('APPROACH 2:\n')
print('PYTHON COLLECTS THE KEYWORD ARGUMENTS IN A DICTIONARY\n')
print('MAKE DICT USING PYTHONIC dict(**kwargs) APPROACH\n')
color_data = makedict(red = 1, green = 2, blue = 3)
print('color_data using makedict keyword arguments : \n', color_data, '\n')    
color_data = dict(red = 1, green = 2, blue = 3)
print('color_data using pythonic dict keyword arguments : \n', color_data, '\n')
print('*****************************************************\n')

# make dict using iterable approach
print('APPROACH 3:\n')
print('MAKE DICT USING PYTHONIC dict(iterable) APPROACH\n')
color_list_iterable = [('red',1), ('green',2),('blue',3)]
color_tuple_iterable = (('red',1), ('green',2),('blue',3))
color_set_iterable = {('red',1), ('green',2),('blue',3)}

col_data = dict(color_list_iterable)
print('col data using pythonic dict list-iterable approach : \n', col_data, '\n')
col_data = dict(color_tuple_iterable)
print('col data using pythonic dict tuple-iterable approach : \n', col_data, '\n')
col_data = dict(color_set_iterable)
print('col data using pythonic dict set-iterable approach : \n', col_data, '\n')
print('*****************************************************\n')


#constructing iterables for dict(iterable) using zip
print('APPROACH 4:\n')
print('CONSTRUCTING ITERABLES FOR dict(iterable) USING zip\n')
print('MAKE DICT USING PYTHONIC dict(iterable) APPROACH\n')

coffee_type = ['C1', 'C2', 'C3']
units_sold = [110, 120, 130]
print('coffee_type : ', coffee_type, '\n')
print('units_sold : ', units_sold, '\n')
print('coffee sales iterable : ', zip(coffee_type, units_sold), '\n')
print('coffee sales list-iterable : ', list(zip(coffee_type, units_sold)), '\n')
print('coffee sales tuple-iterable : ', tuple(zip(coffee_type, units_sold)), '\n')
print('coffee sales set-iterable : ', set(zip(coffee_type, units_sold)), '\n')

coffee_data = dict(zip(coffee_type, units_sold))
print('coffee sales dict using dict(zip(list_1,list_2)) : \n',coffee_data, '\n')
print('*****************************************************\n')

#constructing iterables for dict(iterable) using zip
print('APPROACH 5:\n')
print('Case 1: updating an existing dictionary using keyword arguments\n')
print('Case 2: creating a dictionary using arguments in (k,v) form and keyword arguments\n')
print('UPDATING DICTIONARY USING d.update(**kwargs)\n')

def dodict(*args, **kwargs):
    d = {}
    
    for k, v in args:
        d[k] = v
    
    d.update(kwargs)
    return d

print('key-value pairs in data dictionary : \n', *data.items(), '\n') # returns tuples
print('now adding yellow and updating green value \n')
data_color = dodict(*data.items(), yellow = 2, green = 4)
print('new dictionary with aforementioned changes : \n',data_color, '\n')
print('*****************************************************\n')

print('APPROACH 6:\n')
print('SIMILAR TO APPROACH 5, BUT USES dict(args) FOR INITIAL DICT ASSIGNMENT\n')
print('UPDATING DICTIONARY USING d.update(**kwargs)\n')

def dodict_alternative(*args, **kwargs):
    d = {}
    
    d = dict(args)
    d.update(kwargs)
    return d

print('data dictionary :\n', data, '\n')
print('adding pink and purple to create a new dictionary\n')
color_again = dodict(*data.items(), pink = 2, purple = 4)
print(color_again)
print('*****************************************************\n')