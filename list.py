"""
Problem-Solving:

1. Write a Python program to find the largest number in a list.
2. Write a Python program to sort a list in ascending order without using the built-in sort() method.
3. Write a Python program to find the sum of all the elements in a list.
4. Write a Python program to merge two lists and remove duplicates.
5. Write a Python program to rotate a list by n positions to the right.

"""

"""
Create a 2D-list representing a 3x3 matrix with numbers from 1 to 9. Print the matrix.
Write a Python code to access the element in the second row and third column of the matrix you created.
Write a Python code to modify the element in the first row and second column to 10.
Write a Python code to print all the elements in the 2D-list row by row.
Write a Python code to find the sum of all elements in each row of a 2D-list.
"""

def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

print(sumList([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4 + 5)