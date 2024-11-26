# # program_1 - arithmetic operation
import numpy as np
arr=np.array([1,2,3,4,5])
print("array:",arr)
print("add 5:",arr+5)
print("multiply by 2:",arr*2)
# # program_2 - statistical operations


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("mean:",np.mean(arr))
print("median:",np.median(arr))
print("standard deviation:",np.std(arr))


# # program_3 - reshaping arrays

# In[7]:


import numpy as np
arr=np.arange(1,13)
reshape_arr=arr.reshape(3,4)
print("reshaped array:",reshape_arr)


# # program_4 - array indexing and slicing

# In[8]:


import numpy as np
arr=np.array([10,20,30,40,50])
print("first element:",arr[0])
print("last element:",arr[-1])
print("slice(1 to 3):",arr[1:4])


# # program_5 - array concatenation

# In[9]:


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
con=np.concatenate((arr1,arr2))
print("concatenated array:",con)


# # program_6 - boolean indexing

# In[10]:


import numpy as np
arr=np.array([1,2,3,4,5])
filt_arr=arr[arr>2]
print("filtered array:",filt_arr)


# # program_7 - dot product

# In[11]:


arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
dot_product=np.dot(arr1,arr2)
print("dot product",dot_product)


# # program_8 - linear algebra

# In[14]:


import numpy as np
matrix=np.array([[1,2],[3,4]])
determinant=np.linalg.det(matrix)
inverse=np.linalg.inv(matrix)
print("determinant",determinant)
print("inverse",inverse)






