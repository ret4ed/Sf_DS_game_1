import numpy as np
def shuffle_seed(array):
    seed = np.random.randint(2 ** 32, dtype=np.uint32)
    np.random.seed(seed)
    result = np.random.permutation(array)
    return result, int(seed)
array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
    

