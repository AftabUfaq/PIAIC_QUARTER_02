# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ObSB0EOAJOYtiMX4mZo2grRSUjDkc9PO
"""

import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x

# task 2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))     
    #wrtie your code here
    return x

#task 3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    g = np.array([])
    i = 0 
    for cell in numpy.nditer(a):
      if(cell % 35 == 0):
        g = np.append(g, cell)
    return g

# task 4
def function4():
    #Swap columns 1 and 2 in the array arr.   
    arr = np.arange(9).reshape(3,3)
    arr[:,[0, 1]] = arr[:,[1, 0]]
    return  (arr)

#task 5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
    z = np.full((4,5),0)
    return z

#task 6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
    arr =  np.zeros(10)
    arr[4] = 10
    arr[7] = 20
    return arr

#task7
def function7():
    x = np.arange(4, dtype=np.int64)
    return np.zeros_like(x)

#task 8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    x = np.full((2, 5), 6, dtype=np.uint)
    return x

#task 9   
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    a = np.arange(2,101,2)
    return a

#task 10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-brr[:,None] 
  
    return subt

#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ans = arr[arr%2 == 1] = -1 
    return ans

#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    arr = np.array([1,2,3])
    ans1 = np.dstack((arr,arr,arr)).flatten()
    ans2 = np.hstack((arr,arr,arr))
    ans = np.concatenate((ans1, ans2), axis=None) 
    return ans

#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5)*(arr<10)] 
    return ans

#task14
def function14():
    arr = np.arange(10, 34, 1) #write reshape code
    ans = np.split(arr, 4) 
    return ans

#task15
def function15():
    #Sort following NumPy array by the second column
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = arr[arr[:,1].argsort()]
    return ans

#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.concatenate((x, y), axis=1)  
  
    return ans

#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    arr = np.where((arr %  3 == 0) & (arr % 5 == 0) , 'YES', 'NO') 
    return arr

#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = np.count_nonzero((np.intersect1d(students, piaic)) )
    return x

# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X =   np.arange(1, 26, 1).reshape(5,5) 
    W =  X.transpose() # Write your code here 
    b =  5 # Write your code here
    return (X*W)+b

#Task20
def function20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    g = np.array([])
    def abc(x):
        return x*2+3-2
    for cell in np.nditer(x):
      g = abc(x)
    return g