import numpy as np

keep_Prob = 0.8
a3 = np.arange(1,10).reshape(3,3)
d3 = np.random.rand(a3.shape[0],a3.shape[1]) < keep_Prob

a3 = np.multiply(a3,d3)

a3 = keep_Prob
print(d3,a3)