import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4]) # x points
y = np.array([4,10,2,5]) # y points


plt.title("Marks of Students")
plt.xlabel("students")
plt.ylabel("marks")
plt.plot(x,y, '*:b')
plt.show()