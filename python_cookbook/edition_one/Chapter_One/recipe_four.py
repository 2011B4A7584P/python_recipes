# Chapter 1

# Section 1.4
# Getting a value from a dictionary

# Problem context : We want to obtain a value from a dictionary,
# without having to handle an exception if the key for which the value is
# being sought is not in the dictionary

# Approach 1 
print()
print('APPROACH 1:\n')
print('checking for key membership in dict \n')

colors = dict(red = 1, green = 2, blue = 3)
print('colors : ', colors)

def get_value_from_dict(dictionary, key):
    try:
        if dictionary.has_key(key):
            print(dictionary[key])
        else:
            print(key, 'not found\n')
    except Exception as e:
        print('\nException type : {}\n'.format(type(e).__name__))
        print('\nException message : {}\n'.format(e))

    try:
        if key in dictionary:
            print('Value of {} in dictionary : '.format(key), dictionary[key])
        else:
            print(key, 'not found\n')
    except Exception as e:
        print('\nException type : {}\n'.format(type(e).__name__))
        print('\nException message : {}\n'.format(e))


get_value_from_dict(colors, 'purple')  
print('*****************************************************\n') 
# Approach 2
print()
print('APPROACH 2:\n')
print('using get method dict.get()')
print('dict.get() IS EXTREMELY USEFUL IN ITERATING THROUGH DATA STRUCTURES\n')     

def get_value_from_d(dictionary, key):
    return (dictionary.get(key, '{} not found'.format(key)))

print('red value : ', get_value_from_d(colors, 'red'), '\n')
print('purple value : ', get_value_from_d(colors, 'purple'), '\n')
print('*****************************************************\n')    