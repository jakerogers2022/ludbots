import matplotlib.pyplot as plt

# Define the file names
file_names = ["fitnessData0", "fitnessData1", "fitnessData2", "fitnessData3", "fitnessData4"]

# Loop through each file
for i, file_name in enumerate(file_names):
    # Open the file and read in the data
    with open(file_name, "r") as f:
        data = f.read().strip().split(",")
        data = [float(d) for d in data[:-1]]

    # Create a list of positions for each data point
    positions = list(range(len(data)))

    # Plot the data against the positions
    plt.plot(positions, data, label="p {}".format(i+1))

# Add a legend to the plot
plt.legend()

plt.xlabel("Generation")
plt.ylabel("Fitness")

# Show the plot
plt.show()
