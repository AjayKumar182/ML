import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data

fig=plt.figure()
sb.boxplot(x)
plt.xlabel("data")
plt.ylabel("target")
plt.title("iris box plot")

plt.show()
