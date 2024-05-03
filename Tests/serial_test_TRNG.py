import numpy as np
import matplotlib.pyplot as plt

def serial_test_from_file(file_path, threshold=0.05):
    """
    Performs a serial test on a sequence of numbers read from a text file.

    Parameters:
    - file_path: path to the text file containing the sequence of numbers
    - threshold: significance level for the test (default is 0.05)

    Returns:
    - is_random: True if the sequence passes the serial test (i.e., correlations are within the threshold), False otherwise.
    - sequence: The sequence of numbers read from the file.
    """

    # Read the sequence of numbers from the text file
    with open(file_path, 'r') as file:
        sequence = [float(line.strip()) for line in file.readlines()]

    # Calculate Pearson correlation coefficient between each number and the number that follows it
    correlations = np.corrcoef(sequence[:-1], sequence[1:])[0, 1]

    # Check if the correlation coefficient is within the threshold
    is_random = abs(correlations) < threshold

    return is_random, sequence

# Example usage:
file_path = 'converted_numbers.txt'  # Replace with the path to your text file
is_random, sequence = serial_test_from_file(file_path)
print("Is the sequence random?", is_random)

# Print sequence statistics
print("Sequence Statistics:")
print("Mean:", np.mean(sequence))
print("Standard Deviation:", np.std(sequence))
print("Minimum Value:", '{:.10f}'.format(np.min(sequence))) 
print("Maximum Value:", np.max(sequence))

# Plot histogram
plt.hist(sequence, bins=20, edgecolor='black')
plt.title("Histogram of Generated Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
