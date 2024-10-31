import numpy as np
print(np.iinfo(np.int16))
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))
a = np.float64(1000)
print(np.finfo(a))
b = a + np.int16(25)
print(type(b))

zeros_3d = np.zeros((5,4,3), dtype=np.float32)
print(zeros_3d.shape)

arr, step = np.linspace(-6, 21, 60, retstep=True)
print(round(step,2))

arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(round(step,2))