# NumPy's main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In NumPy dimensions are called axes. The number of axes is rank

import numpy as np 
a = np.arange(15).reshape(3, 5)
print(a)