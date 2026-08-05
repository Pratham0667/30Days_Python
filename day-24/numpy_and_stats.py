import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

normal_array = np.random.normal(79, 15, 80)
print(normal_array)

sns.set_theme()
plt.hist(normal_array, color="grey", bins=50)
plt.show()

two_dimension_array = np.array([(1,2,3),(4,5,6),(7,8,9)])

np_normal_dis = np.random.normal(5, 0.5, 100)

# min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ', two_dimension_array.mean())
print('median: ', np.median(two_dimension_array))   # Fixed
print('sd: ', two_dimension_array.std())

from scipy import stats

np_normal_dis = np.random.normal(5, 0.5, 1000)

# min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis, keepdims=False))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5

plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()