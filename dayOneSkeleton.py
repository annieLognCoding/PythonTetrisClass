dicta = {"a": 5} 
dictb = {"b": 3}
# print(dicta["a"], dictb["b"])

def switch(dictx, dicty): #5, 3
    temp = dictx["a"] #5
    dictx["a"] = dicty["b"] #3
    dicty["b"] = temp #5

# switch(dicta, dictb)
# print(dicta["a"], dictb["b"])

lista =[1, 2, 3, 4, 5]
#listName[ind] <==ind: position index of the element of the list
# print(lista[3])
# print(lista[2:5]) #[start: end(exclusive)]


strA = "hello"
# print(strA[2:4])

studentA = {"name": "Steven", 
            "grade": 6, 
            "age": 12,
            "favorite subject": "Science"}

print(studentA.values())


###String 1 Problems
"""Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    hello_name('Bob') → 'Hello Bob!'
    hello_name('Alice') → 'Hello Alice!'
    hello_name('X') → 'Hello X!'
"""
def hello_name(str):
    return "Hello " + str +"!"

print(hello_name("Steven"))
"""
Given a string, return a version 
without the first and last char, 
so "Hello" yields "ell". 
The string length will be at least 2.
    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'
"""
def without_end(str):
    return str[1:-1]

"""
Given 2 strings, return their concatenation, 
except omit the first char of each. 
The strings will be at least length 1.
    non_start('Hello', 'There') → 'ellohere'
    non_start('java', 'code') → 'avaode'
    non_start('shotl', 'java') → 'hotlava'
"""
def non_start(str1, str2):
    return str1[1:]+str2[1:]

###List 1 Problems
"""Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
    middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
    middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
    middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""
def middle_way(arr1, arr2):
    return [arr1[1], arr2[1]]

"""Given an array of ints length 3, return the sum of all the elements.
sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""
def sum3(arr):
    return arr[0] + arr[1] + arr[2]

"""
Given an array of ints, return True if the array is length 1 or more and the first element and the last element are equal.
    same_first_last([1, 2, 3]) → False
    same_first_last([1, 2, 3, 1]) → True
    same_first_last([1, 2, 1]) → True

"""
def same_first_last(arr):
    return len(arr) >= 1 and arr[0] == arr[-1]

###String 2 Problems (1 loop)
"""
Return the number of times that the string "hi" appears anywhere in the given string.
    count_hi('abc hi ho') → 1
    count_hi('ABChi hi') → 2
    count_hi('hihi') → 2
"""
def count_hi(str):
  result = 0
  if("hi" in str):
     for l in range(len(str) - 1):
        if str[l:l+2] == 'hi':
           result += 1
  return result


"""
Given a string, return a string where for every char in the original, there are two chars.
    double_char('The') → 'TThhee'
    double_char('AAbb') → 'AAAAbbbb'
    double_char('Hi-There') → 'HHii--TThheerree'

"""
def double_char(str):
  result = ""
  for i in str:
     result += i * 2
  return result


"""Return True if the given string contains an appearance of "xyz" where the 
     is not directly preceded by a period (.). So "xxyz" counts but "x.xyz" does not.
    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True
    'xyz.'
"""
def xyz_there(str):
  if(len(str) < 3): return False
  ind = str.find("xyz")
  return ind == 0 or ind > 0 and str[ind - 1] != "." 

def xyz_there2(str):
  for i in range(0, len(str) - 2):
    if(str[i:i+3] == "xyz" and (i == 0 or str[i-1] != ".")): return True
  return False

def xyz3(str):
    if "xyz" not in str:
        return False
    else:
        a, b = str.split("xyz")
        if a[len(a)-1] != ".":
            return True
        else:
            return False

###List 2 Problems (1 loop)
"""Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
    has22([1, 2, 2]) → True
    has22([1, 2, 1, 2]) → False
    has22([2, 1, 2]) → False"""
def has22(nums):
  for i in range(len(nums) - 1):
     if nums[i] == 2 and nums[i + 1] == 2:
        return True

  return False

"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, 
and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
"""
def centered_average(nums):
  biggest = nums[0]
  smallest = nums[0]
  sum = 0
  for i in nums:
    if i > biggest:
        biggest = i
    if i < smallest:
        smallest = i
    sum += 1
  return ((sum-biggest-smallest)/(len(nums)-2))

def nthSandwich(str):
    return 0

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


# listA = [1, 2, 3, 4, 5]
# print(listA.remove(3)) 
# print(listA)

# listA = [1, 2, 3, 4, 5]
# print(listA.pop(3))
# print(listA)

# ageList = [("cow", 5), ("dog", 98), ("cat", 1)]
# ageDict = {}

# for a in ageList:
#     ageDict[a[0]] = a[1]

# print(ageDict)

# def hasConsecutiveDigits(n):
#     return 0

# def ct1(L): 
#     M, N = L, L+[1] 
#     L[0] = 3 
#     N[2] = 4 
#     L += L 
#     for x in [L, M, N]:
#         print(x)
    
# L = [1, 2]
# print(ct1(L))
# print(L) 


# def ct2(L):
#     M = []
#     R = L[::-1] 
#     for k in R:
#         if(k in L) and (k not in M):
#             L.remove(k)
#             M.append(k) 
#         else:
#             M.append(k%3) 
#             print(M.pop(0)) 
#     return M 

# L = [1, 2, 3]*2
# print(ct2(L)) #3 2 1
# print(L)

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

# print(ct3(range(2, 6)))