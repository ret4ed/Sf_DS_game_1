import numpy as np
np.random.seed(2021)
simple = np.random.rand()
randoms = np.random.uniform(-150, 2021, size = 120)
table = np.random.randint(1, 101, size=(3,2))
even = np.arange(2,17,2)
mix = np.random.permutation(even)
select = np.random.choice(even, size=3, replace=False)
triplet = np.random.permutation(select)
