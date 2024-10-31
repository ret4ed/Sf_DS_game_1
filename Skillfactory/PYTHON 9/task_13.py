import numpy as np
def get_unique_loto(num): 
    lst = []
    sample = np.arange(1,101)
    for i in range(num):
        lst.append(np.random.choice(sample, size=(5,5), replace=False))
    arr = np.array(lst)
    return arr
   
print(get_unique_loto(3))
