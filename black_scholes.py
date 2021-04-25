import numpy as np
from scipy import stats

def call(S,K,r,t,Sigma):
    d1 = (np.log(S/K) + (r + 0.5 * Sigma**2)*t)/(Sigma * np.sqrt(t))
    d2 = d1 - Sigma * np.sqrt(t)
    Call = S * stats.norm.cdf(d1,0.0,1.0) - K * np.exp(-r*t) * stats.norm.cdf(d2,0.0,1.0)
    return Call

def put(S,K,r,t,Sigma):
    d1 = (np.log(S/K) + (r + 0.5 * Sigma**2)*t)/(Sigma * np.sqrt(t))
    d2 = d1 - Sigma * np.sqrt(t)
    Put = - (S * stats.norm.cdf(-d1,0.0,1.0) - K * np.exp(-r*t) * stats.norm.cdf(-d2,0.0,1.0))
    return Put

class BlackScholes:

    def __init__(self, S,K,r,day,Sigma):
        self.S = S
        self.K = K
        self.r = r
        self.t = day / 252
        self.Sigma = Sigma

    def call(self):
        S = self.S
        K = self.K
        r = self.r
        t = self.t
        Sigma = self.Sigma
        return call(S,K,r,t,Sigma)

    def put(self):
        S = self.S
        K = self.K
        r = self.r
        t = self.t
        Sigma = self.Sigma
        return put(S,K,r,t,Sigma)

## Exmaple
# bs = BlackScholes(121, 122, 0.01, 5, 0.3)
# callPrice = BlackScholes(121, 122, 0.01, 5, 0.3).call()
# print(callPrice)
# putPrice = bs.put()
# print(putPrice)