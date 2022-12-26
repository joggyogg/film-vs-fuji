import seaborn as sns
import matplotlib.pyplot as plt

# Data to be plotted
data = [57, 71, 86, 100, 79, 71, 86, 71, 100, 86, 86, 100, 86, 86, 86, 86, 57, 86, 86, 71, 71, 100, 93, 71, 57, 36, 86, 71, 43, 86, 93, 64, 57, 86, 86, 64, 43, 100, 57, 71, 86, 100, 71, 71, 71, 71, 86, 100, 93, 71, 86, 86, 86, 43, 71, 100]
# Create the distribution plot with kde
sns.distplot(data)

# Add a title and x and y labels
plt.title("Smooth Distribution Plot of reddit commenters guessing accuracy")
plt.xlabel("Value")
plt.ylabel("Density")

# Show the plot
plt.show()
