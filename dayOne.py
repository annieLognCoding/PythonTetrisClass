def nthSandwich(str):
    if(len(str) < 2): return False
    sand = str[1:-1]
    return str[0] == str[-1] and (not sand or sand.find(str[0]) == -1)


##TYPES OF ERRORS
#1. Syntax
##Syntax errors occur when the code violates the rules of the programming language, so the code will NOT compile. 

#print("Hello World)

#2. Logical
##Logical errors happen when the code runs without crashing but produces incorrect results. 

def divide(a, b):
    return a * b  

#3. Runtime
##  Runtime errors are detected during the execution of the program, often caused by exceptional conditions that disrupt the normal flow of the program. 

tuple = (1, 2)
# tuple[0] = 3

# print(10/0)

def isPalindrome(str):
    return isPalindromeHelp(str, 0, len(str)-1)

def isPalindromeHelp(str, start, end):
    strLen = end - start + 1
    if(strLen <= 1): return True
    return str[start] == str[end] and isPalindromeHelp(str, start + 1, end - 1)

def rotateStringLeft(str, shift):
    if(len(str) <= 1): return str
    if(shift == 0): return str
    if(shift < 0): return rotateStringLeft(str[-1] + str[:-1], shift + 1)
    return rotateStringLeft(str[1:] + str[0], shift - 1)


listA = [1, 2, 3, 4, 5]
print(listA.remove(3)) #remove does not have a return value
print(listA)

listA = [1, 2, 3, 4, 5]
print(listA.pop(3)) #pop returns the removed value
print(listA)

ageList = [("cow", 5), ("dog", 98), ("cat", 1)]
ageDict = {}

for a in ageList:
    ageDict[a[0]] = a[1]

print(ageDict)

def hasConsecutiveDigits(n):
    if(abs(n) < 10): return False
    currDigit = n % 10
    n //= 10
    nextDigit = n % 10
    return True if currDigit == nextDigit else hasConsecutiveDigits(n)

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