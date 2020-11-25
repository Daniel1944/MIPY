# with open(path, "r") as f:
#    lines = f.readlines()
# for line in lines[:15]:
#    line = line.strip()
#    if line[0] in ["#", "!", "/"]:
#        continue
# print(line.split(" "))


import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\topeni.txt"
data = np.loadtxt(path).transpose()
print(np.unique(data[0]))

plt.plot(data[1][:12], data[2][:12])
plt.show()

year = np.unique(data[0].astype("int"))