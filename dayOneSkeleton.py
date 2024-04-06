###String 1 Problems
def hello_name(str):
    return 0

def without_end(str):
    return 0

def non_start(str1, str2):
    return 0

###List 1 Problems
def middle_way(arr1, arr2):
    return 0

def sum3(arr):
    return 0

def same_first_last(arr):
    return 0


###String 2 Problems
def count_hi(str):
  return 0

def double_char(str):
  return 0

def xyz_there(str):
  return 0

###List 2 Problems
def has22(nums):
  return 0

def centered_average(nums):
  
  return 0

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
    return 0

def rotateStringLeft(str, shift):
    return 0


listA = [1, 2, 3, 4, 5]
print(listA.remove(3)) 
print(listA)

listA = [1, 2, 3, 4, 5]
print(listA.pop(3))
print(listA)

ageList = [("cow", 5), ("dog", 98), ("cat", 1)]
ageDict = {}

for a in ageList:
    ageDict[a[0]] = a[1]

print(ageDict)

def hasConsecutiveDigits(n):
    return 0

def ct1(L): 
    M, N = L, L+[1] 
    L[0] = 3 
    N[2] = 4 
    L += L 
    for x in [L, M, N]:
        print(x)
    
L = [1, 2]
print(ct1(L))
print(L) 


def ct2(L):
    M = []
    R = L[::-1] 
    for k in R:
        if(k in L) and (k not in M):
            L.remove(k)
            M.append(k) 
        else:
            M.append(k%3) 
            print(M.pop(0)) 
    return M 

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

print(ct3(range(2, 6)))