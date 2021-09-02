# Chapter 1

# Section 1.5
# Adding an entry to the dictionary

# Problem context : While working with a dictionary D, you need to use the
# entry D[k] if it is already present, or add a new D[k] if k is not yet
# a key in D

# Approach 1 

print()
words_to_page_number_index = dict(humble = [14,32,12], honest = [1,22,54], blue = [3])
print('Index Dictionary : ', words_to_page_number_index)

print('APPROACH 1:\n')
def get_value_from_dict(dictionary, key):
    print('checking for key membership in dict using has_key()\n')
    try:
        if dictionary.has_key(key):
            print(dictionary[key])
        else:
            print(key, 'not found\n')
    except Exception as e:
        print('\nException type : {}\n'.format(type(e).__name__))
        print('\nException message : {}\n'.format(e))
    
    print('checking for key membership in dict using IN clause\n')
    try:
        if key in dictionary:
            print('Value of {} in dictionary : '.format(key), dictionary[key])
        else:
            print(key, 'not found\n')
    except Exception as e:
        print('\nException type : {}\n'.format(type(e).__name__))
        print('\nException message : {}\n'.format(e))


get_value_from_dict(colors, 'purple')  
get_value_from_dict(colors, 'red')  

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