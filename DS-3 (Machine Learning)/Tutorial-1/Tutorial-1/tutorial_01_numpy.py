# -*- coding: utf-8 -*-
"""Tutorial-01_NumPy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IPMlpx1DcsA3BG9xzzFXZriCGnar7An4

## NumPy Essentials


---



![](https://cdn-images-1.medium.com/fit/t/1600/480/1*cyXCE-JcBelTyrK-58w6_Q.png)


NumPy is a powerful library for numerical computations in Python.

#### Why use NumPy?
NumPy is optimized for numerical computations, making it significantly faster than using standard Python lists for such operations. Its efficient array operations and broadcasting capabilities are crucial for scientific computing, data analysis, and machine learning.



---



#### Advantages Over Python Lists

- **Speed**: NumPy performs operations much faster than Python lists, especially on large arrays, due to memory efficiency and optimized algorithms.

- **Multidimensional Arrays**: NumPy offers multidimensional array data structures for representing vectors and matrices.

- **Optimized Built-in Functions**: NumPy provides optimized mathematical functions that enable fast and concise computations without complex loops.

## The ndarray

At the core of NumPy is the **ndarray** (n-dimensional array).

- An ndarray is a multidimensional array with elements of the same type.

- Unlike Python lists, an ndarray enforces consistent element types.

- If mixed types are provided, NumPy upcasts elements to maintain type consistency.

- 1D arrays are rank 1 arrays, while N-dimensional arrays are rank N.

NumPy's efficiency, multidimensional arrays, and optimized functions make it a vital tool for numerical computations in Python.

# Installing NumPy

The only prerequisite for installing NumPy is Python itself. If you don’t have Python yet and want the simplest way to get started, we recommend you use the Anaconda Distribution - it includes Python, NumPy, and many other commonly used packages for scientific computing and data science.

NumPy can be installed using various methods: with conda, with pip, with a package manager on macOS and Linux, or from source. For more detailed instructions, consult our Python and NumPy installation guide below.

## Conda

If you use conda, you can install NumPy from the defaults or conda-forge channels:

```
# Best practice, use an environment rather than installing in the base env
conda create -n my-env
conda activate my-env

# If you want to install from conda-forge
conda config --env --add channels conda-forge

# The actual installation command
conda install numpy
```

## Pip

```
# Create a virtual environment named "my-env"
python -m venv my-env

# Activate the virtual environment
# On Windows:
my-env\Scripts\activate
# On macOS and Linux:
source my-env/bin/activate

# Now your terminal prompt should change to indicate that you're in the virtual environment

# Install NumPy using pip
pip install numpy

# Deactivate the virtual environment when you're done
deactivate
```
"""

!pip install numpy

import numpy as np
print(np.__version__)

"""# Arrays in NumPy"""

# Creating an array from a list
my_list = [1, 2, 3, '4', 5]
my_array = np.array(my_list)
print(my_array)

# Create a 1D ndarray that contains only integers
# Specify the dtype when creating the ndarray
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)
print('x = ', x)
print('x has dimensions:', x.shape) # x has dimensions: (5,)
print('The elements in x are of type:', x.dtype) # The elements in x are of type: int64

## inserttion
# Append
# np.append(ndarray, elements, axis)
## default axis is axis 0: along the rows
# append the integer 6 to x
x = np.append(x, 6)
x

# append to axis 1
x = np.append(x, [6,9,69])
x

"""H/W: Explore method: insert

To represent the numpy array Y mathematically:

\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
10 & 11 & 12 \\
\end{bmatrix} \
"""

# Create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('Y has dimensions:', Y.shape) # Y has dimensions: (4, 3)
print('Y has a total of', Y.size, 'elements') # Y has a total of 12 elements
print('Y is an object of type:', type(Y)) # Y is an object of type: class 'numpy.ndarray'
print('The elements in Y are of type:', Y.dtype) # The elements in Y are of type: int64

"""```
numpy.zeros(shape, dtype=float, order='C', *, like=None)
```
"""

# array of zerps
X = np.zeros((3,4))
X

# array of ones
X = np.ones((6,9))
X

X = np.full((2,3), 5)
X

# Identity Matrix
# Since all Identity Matrices are square, the np.eye() function only takes a single integer as an argument
# 5 x 5 Identity matrix
X = np.eye(5)
X

# Diagonal Matrix
# 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50 on its main diagonal
X = np.diag([10,20,30,50])

"""#### Arange"""

# Arange
# rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)
x

"""![](https://i.imgflip.com/3vuy9v.png?a470208)

##### [The magical link](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
"""

# rank 1 ndarray that has sequential integers from 4 to 9
# [start, stop)
x = np.arange(4,10)
x

# rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
x = np.arange(1,14,3)
x

"""H/W <br>
Explore some similar functions: np.linspace,

#### Reshape
"""

# Reshape
# np.reshape(ndarray, new_shape)
# converts the given ndarray into the specified new_shape
x = np.arange(20)
x

x = np.reshape(x, (4,5))
x

## Or
## specify any one of the dimension as -1 that means
## np will auto calculate it basd on other dimensions
x = np.reshape(x, (-1,5))
x

# or
x = np.arange(20).reshape(4, 5) # does the same thing as above
# One great feature about NumPy, is that some functions can also be
# applied as methods. This allows us to apply different functions in
# sequence in just one line of code
x

"""#### Indexing and Slicing Arrays
Accessing elements and slicing arrays is similar to Python lists:
"""

# Slicing
# ndarray[start:end]
# ndarray[start:]
# ndarray[:end]
# ndarray[<start>:<stop>:<step>]

# In methods one and three, the end index is excluded [,)
## Now guess the output
X = np.arange(20).reshape(4, 5)
X

# select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
Z = X[1:4,2:5]
Z

# or
Z = X[1:,2:5]
Z

# elements = a_list[<start>:<stop>:<step>]
# select all the elements in the 3rd row
v = X[2,:]
print("v =",v)

# select all the elements in the 3rd column
q = X[:,2]
print("q =",q)

# select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]
print("R=",R)

"""Let's Test"""

## give a code for selecting all the elements from second row to second last and first column to third colum
# R = X[?:?,?:?]
# print("R=",R)



# Note: Slicing creates a view, not a copy
# when we make assignments, such as: Z = X[1:4,2:5]
# the slice of the original array X is not copied in the variable Z.
# Rather, X and Z are now just two different names for the same ndarray.
# We say that slicing only creates a view of the original array.
# This means if we make changes to Z, X changes as well.

"""#### Stacking"""

# NumPy also allows us to stack ndarrays on top of each other,
# or to stack them side by side. The stacking is done using either
# the np.vstack() function for vertical stacking, or the np.hstack()
# function for horizontal stacking. It is important to note that in
# order to stack ndarrays, the shape of the ndarrays must match.
x = np.array([1,2])
Y = np.array([[3,4],[5,6]])

z = np.vstack((x,Y)) # [[1,2], [3,4], [5,6]]
z

w = np.hstack((Y,x.reshape(2,1))) # [[3,4,1], [5,6,2]]
w

"""#### Math Functions

Some of the basic methods numpy provides
```
np.add(X,Y)
np.subtract(X,Y)
np.multiply(X,Y)
np.divide(X,Y)

# apply mathematical functions to all elements of an ndarray at once
np.exp(x)
np.sqrt(x)
np.power(x,2)
```
"""

# in order to do these operations the shapes of the ndarrays
# being operated on, must have the same shape or be broadcastable
X = np.array([1,2,3,4]).reshape(2,2)
X

## Statistical Functions
# Statistical Functions
print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Standard Deviation of all elements in X:', X.std())
print('Median of all elements in X:', np.median(X))
print('Maximum value of all elements in X:', X.max())
print('Minimum value of all elements in X:', X.min())

"""#### Understanding axis Parameter

![](https://www.sharpsightlabs.com/wp-content/uploads/2018/12/numpy-arrays-have-axes_updated_v2.png)
"""

matrix = np.array([[1, 2, 3], [4, 5, 6]])
matrix

# Calculate sum along columns (axis=0) and rows (axis=1)
print(np.sum(matrix, axis=0))

print(np.mean(matrix, axis=1))

"""#### Matrix Multiplication (matmul)"""

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

matrix_a

matrix_b

result = np.matmul(matrix_a, matrix_b)
print(result)

"""#### Outer and Inner Products"""

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

outer_product = np.outer(vector_a, vector_b)
inner_product = np.inner(vector_a, vector_b)

print(outer_product) # bT.a -> 3X1 1X3

print(inner_product) ## aT.b

"""### Converting Pandas DataFrame to NumPy Array

Why Convert? <br>
NumPy arrays are more suitable for numerical operations, while DataFrames are versatile data structures for data manipulation.
"""

import pandas as pd
## one way of creating df from dictionary
## very useful in long run
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
df.head()

# Convert DataFrame to NumPy array
numpy_array = df.to_numpy()
print(numpy_array)

"""#### Some other methods"""

# Broadcasting
# NumPy allows operations between arrays of different shapes, known as broadcasting:

a = np.array([1, 2, 3])
b = 2

result = a + b
print(result)

"""##### **A universal function (or ufunc for short)** is a function that operates on ndarrays in an element-by-element fashion, supporting array broadcasting, type casting, and several other standard features.

![](https://i.redd.it/nklty63uzav41.png)
"""

def complex_array_function(input_array):
    return np.sqrt(np.mean(np.square(np.abs(input_array))))

# Example input array
input_array = np.array([-2, 4, -6, 8, -10])
input_array

# Calling the complex function
result = complex_array_function(input_array)
print("Result:", result)

"""##### Random"""

# Random
# 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
# np.random.random(shape)
X = np.random.random((3,3))
X

# np.random.randint(start, stop, size = shape)
# [start, stop)
X = np.random.randint(4,15,size=(3,2))
X

# create ndarrays with random numbers that satisfy certain statistical properties
# 1000 x 1000 ndarray of random floats drawn from normal (Gaussian)
# distribution with a mean of zero and a standard deviation of 0.1.
# np.random.normal(mean, standard deviation, size=shape)
X = np.random.normal(0, 0.1, size=(1000,1000))

"""And many more such fuction to genrate random values, also you might have used such function in DS 2 Lab like numpy.random.choice, Have You?"""

## using same seed will force pseudo random generator to gernetrate same number
# np.random.seed(32)
x = np.random.randint(0,5)
x

"""![](https://i.pinimg.com/736x/3e/9e/86/3e9e86d7727f436596e5216a82c74b29.jpg)"""