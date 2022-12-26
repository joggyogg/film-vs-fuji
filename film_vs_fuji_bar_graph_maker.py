import matplotlib.pyplot as plt

# List of lists with bar name, bar color, top bar, and bottom bar
image_data = [
    ["1", "red", [47, 0], [0,-9]],
    ["2", "blue", [3, 0], [0, -53]],
    ["3", "red", [38, 0], [0, -18]],
    ["4", "blue", [24, 0], [0, -32]],
    ["5", "red", [49, 0], [0, -7]],
    ["6", "blue", [16, 0], [0, -40]],
    ["7", "blue", [4, 0], [0, -52]],
    ["8", "red", [46, 0], [0, -10]],
    ["9", "red", [41, 0], [0, -15]],
    ["10", "blue", [10, 0], [0, -46]],
    ["11", "red", [39, 0], [0, -17]],
    ["12", "blue", [18, 0], [0, -38]],
    ["13", "blue", [10, 0], [0, -46]],
    ["14", "red", [42, 0], [0, -14]],
]

# Create figure and axis
fig, ax = plt.subplots()

# Set y-axis limits to include the lowest value in the bottom bars
min_bottom = min([x[3][1] for x in image_data])
ax.set_ylim(min_bottom - 5, 55)
ax.set_ylabel('pos = red guesses, neg = blue guesses')

# Add horizontal line at y=0
ax.axhline(y=0, color='black', linewidth=1)

# Set width of bars
bar_width = 0.8

# Set the x-axis tick marks to be the bar names
ax.set_xticks([i for i in range(len(image_data))])
ax.set_xticklabels([x[0] for x in image_data])

# Iterate through each list and plot the top and bottom bars
for i, data in enumerate(image_data):
    name, color, top, bottom = data
    if color == "red":
        top_color = "red"
        bottom_color = "pink"
    else:
        top_color = "lightblue"
        bottom_color = "blue"
    ax.bar(i, top[0]-bottom[0], bar_width, bottom=bottom[0], color=top_color)
    ax.bar(i, bottom[1]-bottom[0], bar_width, bottom=bottom[0], color=bottom_color)

plt.title("""Number of film and digital Guesses per Image,
red bars are film, blue bars are digital""")
plt.show()
