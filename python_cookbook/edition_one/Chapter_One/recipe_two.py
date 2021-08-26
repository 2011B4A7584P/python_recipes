# Chapter 1

# Section 1.2
# Swapping values without using a temporary variable

# Python's automatic tuple packing (happens on the right side)
# and unpacking are used to achieve swap readily

a,b,c = 1,2,3
print("pre swap values")
print('a : {}, b : {}, c : {}'.format(a,b,c))
a,b,c = b,c,a
print("post swap values")
print('a : {}, b : {}, c : {}'.format(a,b,c))

# Tuple packing, done using commas, on the right hand side and 
# sequence (tuple) unpacking, done by placing several comma-separated 
# targets on the lefthand side of a statement, are both useful, simple
# and general mechanisms
