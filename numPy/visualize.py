# GPT generated code to visualize how numpy stores data in contiguous memory like C style
import matplotlib.pyplot as plt

# Memory addresses (assuming 4 bytes per element)
elements = [10, 20, 30, 40, 50]
memory_addresses = [1000 + (i * 4) for i in range(len(elements))]

# Create a figure
fig, ax = plt.subplots(figsize=(8, 3))

# Plot memory layout
for i in range(len(elements)):
    ax.add_patch(plt.Rectangle((memory_addresses[i], 0), 4, 1, edgecolor='black', facecolor='lightblue'))
    ax.text(memory_addresses[i] + 2, 0.5, str(elements[i]), ha='center', va='center', fontsize=12, color='black')

# Add arrow to indicate pointer to first element
ax.annotate("Pointer to first element", xy=(memory_addresses[0], 0.5), xytext=(memory_addresses[0] - 40, 1.5),
             arrowprops=dict(facecolor='red', arrowstyle="->"), fontsize=12, color='red')

# Labels and Formatting
ax.set_xlim(memory_addresses[0] - 50, memory_addresses[-1] + 10)
ax.set_ylim(-1, 2)
ax.set_xticks(memory_addresses)
ax.set_xticklabels(memory_addresses)
ax.set_yticks([])
ax.set_title("NumPy Array Contiguous Memory Layout", fontsize=14)
ax.set_xlabel("Memory Address", fontsize=12)

# Show the plot
plt.show()
