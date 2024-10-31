import numpy as np
def get_chess(a):
    chess = np.zeros((a,a), dtype=np.float16)
    for i in range(a):
        if i%2 == 0:
            chess[i][1::2] = 1
        else:
            chess[i][::2] = 1
    return chess
print(get_chess(24))