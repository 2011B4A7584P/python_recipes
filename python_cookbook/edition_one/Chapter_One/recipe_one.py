# Chapter 1

# Section 1.1
'''
apply() in Python 2 and earlier

Description
Returns the result of a function or class object called with 
supplied arguments

Syntax
apply (function, args[, kwargs])

function
--------
Required. The function argument must be a callable object 
(a user-defined or built-in function or method, or a class object).

args
----
Required. A sequence of positional arguments.

kwargs
------
Optional. The kwargs argument must be a dictionary whose keys are strings. 
It specifies keyword arguments to be added to the end of the argument list.
'''

# Example 1
def bar(a, b, c=None):
     return a, b, c

try:
    print(apply(bar, (1, 2), {'c': 3})) # Works with Python 2 or lesser only
    # Output
    # (1, 2, 3)
except NameError:
     print("bar implementation through apply : ","apply works with Python 2 or lesser only")


# Example 2
def check_prime(input_number):
    if input_number <= 1:
       return False
    elif input_number == 2:
       return True
    else:
        for i in list(range(2,input_number)):
            if input_number % i == 0:
               return False
    return True    

# Old school way of doing apply         
def some_method_1(*args, **kwargs):
    '''
    apply function below is obsolete in Python 3
    this implementation would work fine with Python 2 only
    '''
    try:
        print(apply(check_prime, args, kwargs))
    except NameError:
        print("checkprime implementation through apply :", "apply works with Python 2 or lesser only")

# Elegant and more Pythonic way of doing the same        
def some_method_2(*args, **kwargs):
    # Do something with argument
    print(check_prime(*args, **kwargs), " : checkprime modern implementation without apply")
        
print("directly calling function with arguments : ", check_prime(6))
# Output
# False
some_method_1(6) # Works with Python 2 only since apply() is obsolete
# Output
# False
some_method_2(6)
# Output
# False

# Note: 
'''
above use case of apply() is obsolete. 
Use function(*args, **kwargs) instead of apply(function, args, kwargs).
'''