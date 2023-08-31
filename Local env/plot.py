import matplotlib.pyplot as plt
import pandas as pd

results = pd.read_csv("runs/classify/train/results.csv")

# ploting the loss of the training and test sets
plt.figure()
plt.title("The loss of the training and test sets")
plt.plot(results[results.columns[0]], results[results.columns[1]], label="Training loss")
plt.plot(results[results.columns[0]], results[results.columns[4]], label="Validation loss")
plt.legend()
plt.grid()
plt.xlabel("The number of epochs")
plt.ylabel("The loss values")

# ploting the accuracy of the training set
plt.figure()
plt.title("The accuracy of the training set")
plt.plot(results[results.columns[0]], results[results.columns[2]], label="Training accuracy")
plt.legend()
plt.grid()
plt.xlabel("The number of epochs")
plt.ylabel("The accuracy values")
plt.show()