import numpy as np

a = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print a.shape                     # Prints "(2, 3)"
print a[0, 0], a[0, 1], a[1, 0]   # Prints "1 2 4"


#fill array :-
b=np.zeros((2,2))
print b
b=np.ones((2,2))
print b
b=np.full((2,2),5)
b[0,0]=1;
print b
b=np.eye(3,3)							#Identity matrix
print b


#arrange:-
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print a  # prints "array([[ 1,  2,  3],
         #                [ 4,  5,  6],
         #                [ 7,  8,  9],
         #                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print a[np.arange(4), b]  # Prints "[ 1  6  7 11]"


#Boolean array indexing:-
a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.
            
print bool_idx      # Prints "[[False False]
                    #          [ True  True]
                    #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print a[bool_idx]  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print a[a > 2]     # Prints "[3 4 5 6]"

