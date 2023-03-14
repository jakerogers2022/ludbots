import matplotlib.pyplot as plt

# Define the file names
# file_names = ["fitnessData0", "fitnessData1", "fitnessData2", "fitnessData3", "fitnessData4"]
file_name_root = "fitnessDataPHC"
l = 5

phc_averages = []
tk_averages = []
ptk_averages = []

phc_max_fitness = []
tk_max_fitness = []
ptk_max_fitness = []

# Loop through each file
for i in range(10):
    file_name = file_name_root + str(i)
    # Open the file and read in the data
    with open(file_name, "r") as f:
        data = f.read().strip().split(",")
        data = [float(d) for d in data[:-1]]
        phc_averages.append(data)

    # Create a list of positions for each data point
    positions = list(range(len(data)))

    phc_max_fitness.append(data[-1])


    # Plot the data against the positions
    plt.plot(positions, data, label="p {}".format(i+1))

# Add a legend to the plot
plt.legend()
plt.title("PHC")
plt.xlabel("Generation")
plt.ylabel("Fitness")

# Show the plot
plt.show()

file_name_root = "fitnessDataTK"
l = 5

# Loop through each file
for i in range(10):
    file_name = file_name_root + str(i)
    # Open the file and read in the data
    with open(file_name, "r") as f:
        data = f.read().strip().split(",")
        data = [float(d) for d in data[:-1]]
        tk_averages.append(data)

    # Create a list of positions for each data point
    positions = list(range(len(data)))

    tk_max_fitness.append(data[-1])


    # Plot the data against the positions
    plt.plot(positions, data, label="p {}".format(i+1))

# Add a legend to the plot
plt.legend()
plt.title("TK")

plt.xlabel("Generation")
plt.ylabel("Fitness")

# Show the plot
plt.show()

file_name_root = "fitnessDataPTK"
l = 5

# Loop through each file
for i in range(10):
    file_name = file_name_root + str(i)
    # Open the file and read in the data
    with open(file_name, "r") as f:
        data = f.read().strip().split(",")
        data = [float(d) for d in data[:-1]]
        ptk_averages.append(data)

    # Create a list of positions for each data point
    positions = list(range(len(data)))

    ptk_max_fitness.append(data[-1])


    # Plot the data against the positions
    plt.plot(positions, data, label="p {}".format(i+1))

# Add a legend to the plot
plt.legend()
plt.title("PTK")
plt.xlabel("Generation")
plt.ylabel("Fitness")

# Show the plot
plt.show()


avg_phc_values = [sum(pos)/len(pos) for pos in zip(*phc_averages)]
avg_tk_values = [sum(pos)/len(pos) for pos in zip(*tk_averages)]
avg_ptk_values = [sum(pos)/len(pos) for pos in zip(*ptk_averages)]

# Plot the average PHC values
plt.plot([0]+avg_phc_values, label='PHC')

# Plot the average TK values
plt.plot([0]+avg_tk_values, label='TK')

# Plot the average PTK values
plt.plot([0]+avg_ptk_values, label='PTK')

# Add labels and legend to the plot
plt.xlabel('Position')
plt.ylabel('Average Value')
plt.title('Average Values for PHC, TK, and PTK')
plt.legend()

# Display the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Define the fitness values for each algorithm
algo1 = phc_max_fitness
algo2 = tk_max_fitness
algo3 = ptk_max_fitness

# Perform ANOVA
fvalue, pvalue = f_oneway(algo1, algo2, algo3)

# Print the results
print("F-value:", fvalue)
print("P-value:", pvalue)

# Plot the histograms
kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})

plt.figure(figsize=(10,7), dpi= 80)
sns.distplot(algo1, color="dodgerblue", label="PHC", **kwargs)
sns.distplot(algo2, color="orange", label="TK", **kwargs)
sns.distplot(algo3, color="green", label="PTK", **kwargs)

plt.xlim(0,35)
plt.legend()
plt.title("Distribution of Fitness Values for Three Evolutionary Algorithms Across 50 Generations")
plt.xlabel("Fitness Value")
plt.ylabel("Density")
plt.show()
