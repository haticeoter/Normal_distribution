from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
x_rvs=norm.rvs(loc=0, scale=1, size=50)
mu, sigma= norm.fit(x_rvs)
x=np.linspace(-5,5,10)
fig, ax=plt.subplots(figsize=(16,6))
ax.hist(x_rvs, bins=50, density= True, color='red', rwidth=0.8)
ax.plot(x, norm.pdf(x, loc=mu, scale=sigma),lw=5)
ax.plot(x, norm.cdf(x, loc=mu, scale=sigma),lw=5)
plt.xlabel("X random variables")
plt.ylabel("Values")
plt.show()
print("mean value of X rvs=", norm.mean(mu, sigma))
print("standart deviation of X rvs=", norm.std(mu, sigma))

