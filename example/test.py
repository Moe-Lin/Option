import numpy as np
from scipy import stats
from matplotlib import pyplot as plt 

x = np.arange(0,11) 

S = 100.
K = 105.
r = 0.01
#t = 180/252.
t = x
Sigma = 0.2

d1 = (np.log(S/K) + (r + 0.5 * Sigma**2)*t)/(Sigma * np.sqrt(t))
d2 = d1 - Sigma * np.sqrt(t)

Call = S * stats.norm.cdf(d1,0.0,1.0) - K * np.exp(-r*t) * stats.norm.cdf(d2,0.0,1.0)

print(Call);

y = Call


plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()