# Return the number of even integers in the given array.

def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0: count += 1
    return count 


"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
"""
def big_diff(nums):
    return max(nums) - min(nums)

"""
Return the "centered" average of an array of ints, 
which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. You may assume that the array is length 3 or more.
"""
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)

"""
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""
def sum13(nums):
    result = 0
    turnOn = False
    for i in range(len(nums)):
        print(i)
        if(nums[i] == 13 or turnOn):
            turnOn = True
            if(i < len(nums) - 1):
                turnOn = False
            continue
        result += nums[i]
    return result

print(sum13([1, 2, 13, 2, 1, 13]))

"""
Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.
"""
def sum67(nums):
    result = 0
    span = False
    for i in nums:
        if i == 6:
            span = True
        if not span:
            result += i
        if i == 7:
            span = False
    return result

"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
"""
def has22(nums):
    for i in range(len(nums)-1):
        if(nums[i] == 2 and nums[i +1] == 2):
            return True
    return False


def func_foo(s):
    length = len(s)
    result = ""
    for i in range(length):
        if s[i] == s[length - 1 - i]:
            result += s[i]
        else:
            break
    return result
print(func_foo("abXYZba"))
print(func_foo("racecar"))
print(func_foo("hello"))

def linear_in(outer, inner):
    outer_len = len(outer)
    inner_len = len(inner)
    
    outer_index = 0
    inner_index = 0
    
    while outer_index < outer_len and inner_index < inner_len:
        if outer[outer_index] == inner[inner_index]:
            inner_index += 1
        outer_index += 1
    
    return inner_index == inner_len
print(linear_in([1, 2, 4, 6], [2, 4])) 
print(linear_in([1, 2, 4, 6], [2, 3, 4]))
print(linear_in([1, 2, 4, 4, 6], [2, 6])) 