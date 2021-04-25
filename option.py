import numpy as np
import black_scholes as bs

from matplotlib import pyplot as plt

x = np.arange(1,20)
# x = 5

S = 121
# S = 117 + x
#K = 122
low = 118
center = 121
hight = 124
r = 0.01
day = 5
# Sigma = 0.3
Sigma = 0.1*x

call_low = bs.BlackScholes(S, 118, r, day, Sigma).call()
call_center = bs.BlackScholes(S, 121, r, day, Sigma).call()
call_hight = bs.BlackScholes(S, 124, r, day, Sigma).call()

price = call_low - 2*call_center + call_hight
max_profit = center - low - price
# print("Butterfly Price: " + str(price) )
# print("Max Profit: " + str(max_profit) )


## matplotlib
y = price
plt.title("IV-Price")
plt.xlabel("IV")
plt.ylabel("Option Price")
plt.plot(Sigma,y)
plt.show()