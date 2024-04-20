# 2D LISTS

#1. Creating 2D lists

# create a 2d list with fixed values (static allocation)
a = [ [ 2, 3, 4 ] , [ 5, 6, 7 ] ]
print(a)

#2. Dynamic Allocation

#WRONG! DO NOT SHALLOW COPY!!

# Try, and FAIL, to create a variable-sized 2d list
rows = 3
cols = 2

a = [ [0] * cols ] * rows # Error: creates shallow copy
                          # Creates one unique row, the rest are aliases!
 
print("This SEEMS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("But see what happens after a[0][0]=42")
print("   a =", a)