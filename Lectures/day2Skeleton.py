##### for loops #####

# def func1(m, n):
#     total = 0
#     # note that range(x, y) includes x but excludes y
#     for x in range(2, 12, 3):
#         total += x
#     return total

# print(func1(2, 12))

# #"range" obejct
# print(range(0, 4))
# print(list(range(0, 4)))

# def func1_with_range(m, n):
#     return sum(range(m, n+1))

# print(func1_with_range(5, 10))

# def print_with_range(n, m):
#     print(list(range(n, m+1)))

# print_with_range(5, 10) 



# And we can even do this with a closed-form formula,
# which is the fastest way, but which doesn't really
# help us demonstrate loops.  :-)

# def helper(n):
#     # helper function
#     #returns the sum from 1 - n
#     return n*(n+1)//2

# def func1_with_helper(m, n):
#     #the sum from m to n
#     return helper(n) - helper(m-1)

# print(func1_with_helper(5, 10))


# sum just odd numbers from m to n
# def func2(m, n):
#     total = 0
#     for i in range(m, n+1):
#         if(i % 2 == 1):
#             total += i
#     return total

# print(func2(4, 10) == func2(5,9) == (5+7+9))

# # another way?

# def func2_with_step(m, n):
#     if (m % 2 == 0):
#         # m is even, add 1 to start on an odd
#         m += 1
#     total = 0
#     for x in range(m, n+1, 2):
#         total += x
#     return total

# def func2_with_range(m,n):
#     if m%2==1:
#         return (sum(range(m,n+1,2)))
#     return (sum(range(m+1,n+1,2)))

# print(func2_with_step(4, 10) == func2_with_range(5,9) == (5+7+9))


# # Here we will range in reverse
# # (not wise in this case, but instructional)

# def func2_in_reverse(m, n):
#     return 0

# print(func2_in_reverse(4, 10) == func2_in_reverse(5,9) == (5+7+9))

### Nested For Loops ###

# def func3(n, m):
#     for i in range(n+1): #i: 0~n i = 2
#         for j in range(m+1): #j: 0~m
#             print("(", i, ",", j, ")  ", end="")
#         print() #new line

# func3(4, 5)
# func3(2, 2)

# how about some stars?
## What does this Print?
# def func4(n):
#     for row in range(n): #row: 0-4
#         for col in range(n): #col: 0-4
#             print("*", end="")
#         print()

# func4(5)

# What would this do? Be careful and be precise!

# def func5(n):
#     for row in range(n): #row: 0 - (n-1), row: 1
#         print(row, end=" ")
#         for col in range(row): #col, 
#             print("*", end=" ")
#         print()

# #0  
# #1 *
# #
# func5(5)

### While Loops ###

# use while loops when there is an indeterminate number of iterations

# def func6(n):
#     n = abs(n)
#     while (n >= 10): #until n < 10
#         n = n//10
#     return n

# print(func6(72658489290098))

# def reverseDigits(n):
#     #7265 = 7*10^3 + 7*10^2 + 7*10 + 5
#     #5627 = 5*10^3 + 6*10^2 + 2*10 + 7
#     reversed = 0

#     while(n != 0): #5627
#         digit = n % 10
#         reversed = reversed * 10 + digit
#         n = n // 10

#     return reversed

# print(reverseDigits(1234))
# assert(reverseDigits(7265) == 5627)


# nth positive integer with some property
# eg: find the nth number that is a multiple of either 4 or 7
# def isMultipleOf4or7(x):
#     return ((x % 4) == 0) or ((x % 7) == 0)
 
# def func7(n):
#     found = 0
#     guess = -1
#     #Why do we use while loop here?
#     while (found <= n):
#         guess += 1
#         if (isMultipleOf4or7(guess)):
#             found = found + 1
#     return guess

# print("Multiples of 4 or 7: ", end="")
# for n in range(5): #0 1 2 3 4
#     print(func7(n), end=" ")
# print()

## Can you identify the bug?

# def buggySumToN(n):
#     # note: this not only uses a "while" instead of a "for" loop,
#     # but it also contains a bug. Ugh.
#     total = 0
#     counter = 0
#     while (counter <= n): #counter: 0 ~ n
#         total += counter
#         counter += 1

#     return total

# print(buggySumToN(5))


# break and continue
# for n in range(200):
#     if (n % 3 == 0):
#         continue # skips rest of this pass (rarely a good idea to use "continue")
#     elif (n == 8):
#         break # skips rest of entire loop
#     print(n, end=" ")
# print()

#isPrime

# Note: there are faster/better ways.  We're just going for clarity and simplicity here.
# def func8(n):
#     if (n < 2):
#         return False
#     for factor in range(2,n):
#         if (n % factor == 0):
#             return False
#     return True

# # And take it for a spin
# for n in range(100):
#     if func8(n):
#         print(n, end=" ")
# print()
"""
#fasterisPrime
#Note: this is still not the fastest way, but it's a nice improvement.
def faster_func8(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

#nth Prime

def nthPrime(n):
    return 0

# and let's see a list of the primes
for n in range(10):
    print(n, nthPrime(n))
print("Done!")

### Reading Practice ###
def ct1(L): #L is passed by reference
    M, N = L, L+[1] #M points to L, N is created a new reference
    L[0] = 3 #[3, 2]
    N[2] = 4 #[1, 2, 4]
    L += L #[3, 2, 3, 2]
    for x in [L, M, N]:
        print(x)
    
L = [1, 2]
print(ct1(L))
print(L) #[3, 2, 3, 2]


def ct2(L):
    M = []
    R = L[::-1] #[3, 2, 1, 3, 2, 1]
    for k in R:
        if(k in L) and (k not in M):
            L.remove(k)
            M.append(k) #[3, 2, 1]
        else:
            M.append(k%3) #[3, 2, 1, 0] [2, 1, 0, 2] [1, 0, 2, 1]
            print(M.pop(0)) #3 2 1
    return M #[0, 2, 1]

L = [1, 2, 3]*2
print(ct2(L)) #3 2 1
print(L)

def ct3(a):
    (x, result) = (0, [])
    while(sum(result) < 10):
        try:
            result.append(a[x])
            x += 5
        except:
            result.append(1)
            x //= 2
    return result

print(ct3(range(2, 6))) #[2, 1, 4, 1, 5]
"""