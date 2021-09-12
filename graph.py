import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,squares, linewidth =5)

# set title and label axes

plt.title("Title",fontsize=24)
plt.xlabel("X-Value",fontsize=24)
plt.ylabel("Y-Value", fontsize=14)
plt.show()