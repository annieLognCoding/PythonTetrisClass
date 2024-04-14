# ##### for loops #####

# def sumFromMToN(m, n):
#     total = 0
#     # note that range(x, y) includes x but excludes y
#     for x in range(m, n+1):
#         total += x
#     return total
# print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# #"range" obejct
# print(range(0, 4))
# print(list(range(0, 4)))

# def sumFromMToN(m, n):
#     return sum(range(m, n+1))

# print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# # And we can even do this with a closed-form formula,
# # which is the fastest way, but which doesn't really
# # help us demonstrate loops.  :-)

# def sumToN(n):
#     # helper function
#     return n*(n+1)//2

# def sumFromMToN_byFormula(m, n):
#     return (sumToN(n) - sumToN(m-1))

# print(sumFromMToN_byFormula(5, 10) == 5+6+7+8+9+10)


# # sum just odd numbers from m to n
# def sumOfOddsFromMToN(m, n):
#     total = 0
#     for x in range(m, n+1):
#         if (x % 2 == 1):
#             total += x
#     return total

# print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# # another way?

# def sumOfOddsFromMToN(m, n):
#     if (m % 2 == 0):
#         # m is even, add 1 to start on an odd
#         m += 1
#     total = 0
#     for x in range(m, n+1, 2):
#         total += x
#     return total

# print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))


# # Here we will range in reverse
# # (not wise in this case, but instructional)

# def sumOfOddsFromMToN(m, n):
#     if (n % 2 == 0):
#         # n is even, subtract 1 to start on an odd
#         n -= 1
#     total = 0
#     for x in range(n, m-1, -2):  # be careful here!
#         total += x
#     return total

# print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# ### Nested For Loops ###

# # print the cartesian coordinate
# def printCoordinates(xMax, yMax):
#     for x in range(xMax+1):
#         for y in range(yMax+1):
#             print("(", x, ",", y, ")  ", end="")
#         print()

# printCoordinates(4, 5)

# # how about some stars?

# def printStarRectangle(n):
#     # print an nxn rectangle of asterisks
#     for row in range(n):
#         for col in range(n):
#             print("*", end="")
#         print()

# printStarRectangle(5)

# # What would this do? Be careful and be precise!

# def printMysteryStarShape(n):
#     for row in range(n):
#         print(row, end=" ")
#         for col in range(row):
#             print("*", end=" ")
#         print()

# printMysteryStarShape(5)

# ### While Loops ###

# # use while loops when there is an indeterminate number of iterations

# def leftmostDigit(n):
#     n = abs(n)
#     while (n >= 10):
#         n = n//10
#     return n

# print(leftmostDigit(72658489290098) == 7)


# # nth positive integer with some property
# # eg: find the nth number that is a multiple of either 4 or 7
# def isMultipleOf4or7(x):
#     return ((x % 4) == 0) or ((x % 7) == 0)

# def nthMultipleOf4or7(n):
#     found = 0
#     guess = -1
#     while (found <= n):
#         guess += 1
#         if (isMultipleOf4or7(guess)):
#             found += 1
#     return guess

# print("Multiples of 4 or 7: ", end="")
# for n in range(15):
#     print(nthMultipleOf4or7(n), end=" ")
# print()

# ## Can you identify the bug?

# def buggySumToN(n):
#     # note: this not only uses a "while" instead of a "for" loop,
#     # but it also contains a bug. Ugh.
#     total = 0
#     counter = 0
#     while (counter <= n):
#         counter += 1
#         total += counter
#     return total

# print(buggySumToN(5) == 1+2+3+4+5)


# # A for loop is the preferred way to loop over a fixed range.
# def sumToN(n):
#     total = 0
#     for counter in range(n+1):
#         total += counter
#     return total

# print(sumToN(5) == 1+2+3+4+5)

# # break and continue
# for n in range(200):
#     if (n % 3 == 0):
#         continue # skips rest of this pass (rarely a good idea to use "continue")
#     elif (n == 8):
#         break # skips rest of entire loop
#     print(n, end=" ")
# print()

# #isPrime

# # Note: there are faster/better ways.  We're just going for clarity and simplicity here.
# def isPrime(n):
#     if (n < 2):
#         return False
#     for factor in range(2,n):
#         if (n % factor == 0):
#             return False
#     return True

# # And take it for a spin
# for n in range(100):
#     if isPrime(n):
#         print(n, end=" ")
# print()

# #fasterisPrime
# #Note: this is still not the fastest way, but it's a nice improvement.
# def fasterIsPrime(n):
#     if (n < 2):
#         return False
#     if (n == 2):
#         return True
#     if (n % 2 == 0):
#         return False
#     maxFactor = round(n**0.5)
#     for factor in range(3,maxFactor+1,2):
#         if (n % factor == 0):
#             return False
#     return True

# # And try out this version:
# for n in range(100):
#     if fasterIsPrime(n):
#         print(n, end=" ")
# print()

# #nth Prime

# def nthPrime(n):
#     found = 0
#     guess = 0
#     while (found <= n):
#         guess += 1
#         if (isPrime(guess)):
#             found += 1
#     return guess

# # and let's see a list of the primes
# for n in range(10):
#     print(n, nthPrime(n))
# print("Done!")

# ### Reading Practice ###
# def ct1(L): #L is passed by reference
#     M, N = L, L+[1] #M points to L, N is created a new reference
#     L[0] = 3 #[3, 2]
#     N[2] = 4 #[1, 2, 4]
#     L += L #[3, 2, 3, 2]
#     for x in [L, M, N]:
#         print(x)
    
# L = [1, 2]
# print(ct1(L))
# print(L) #[3, 2, 3, 2]


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
print(ct2(L)) 
print(L) #1 2 3

# def ct3(a):
#     (x, result) = (0, [])
#     while(sum(result) < 10):
#         try:
#             result.append(a[x])
#             x += 5
#         except:
#             result.append(1)
#             x //= 2
#     return result

# print(ct3(range(2, 6))) #[2, 1, 4, 1, 5]