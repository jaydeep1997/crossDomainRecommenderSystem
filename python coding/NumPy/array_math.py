import numpy as np

a=np.array([[1,2], [3,4]])
b=np.array([[2,3], [5,9]])

c=a+b
print c				#or np.add(a,b)
print a*b			#or np.multiply(a,b)


#dot and multiplication :-
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print v.dot(w)		#or np.dot(v, w)

# Matrix / vector product; both produce the rank 1 array [29 67]
print x.dot(v)		#is not same as v.dot(x)
print v.dot(x)

# Matrix / matrix product; both produce the rank 2 array (matrix multiplication)
# [[19 22]
#  [43 50]]
print x.dot(y)


#sum :-
x = np.array([[1,2],[3,4]])
print np.sum(x)  # Compute sum of all elements; prints "10"
print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"


#Transpose of a matrix :-
x = np.array([[1,2,5], [3,4,6]])
print x    # Prints "[[1 2]
           #          [3 4]]"
print x.T  # Prints "[[1 3]
           #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print v.T    # Prints "[1 2 3]"
v = np.array([[1,2,3]])
print v.T  # Prints "[1 2 3]"
