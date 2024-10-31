import numpy as np
def get_loto(num): 
    return np.random.randint(0, 101, size=(num,5,5))
print(get_loto(3))