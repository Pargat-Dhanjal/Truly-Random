import numpy as np
from scipy.stats import pearsonr
import os
import matplotlib.pyplot as plt

def autocorrelation_test_from_file(file_path, lag=1, alpha=0.05):
    """
    Performs an Autocorrelation Test on a sequence of numbers read from a text file.

    Parameters:
    - file_path: path to the text file containing the sequence of numbers
    - lag: lag value for autocorrelation calculation (default is 1)
    - alpha: significance level for the test (default is 0.05)

    Returns:
    - is_random: True if the sequence passes the Autocorrelation Test (i.e., autocorrelation coefficient at lag is within the threshold), False otherwise.
    - autocorr_coeff: Autocorrelation coefficient calculated for the sequence.
    - sequence: The sequence of numbers read from the file.
    """

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Read the sequence of numbers from the text file
    with open(file_path, 'r') as file:
        sequence = [float(line.strip()) for line in file.readlines()]

    # Check if sequence has enough data points for the specified lag
    if len(sequence) <= lag:
        raise ValueError("Sequence does not have enough data points for the specified lag.")

    # Calculate autocorrelation coefficient
    autocorr_coeff, _ = pearsonr(sequence[:-lag], sequence[lag:])

    # Check if the autocorrelation coefficient is within the threshold
    is_random = abs(autocorr_coeff) < alpha
    return is_random, autocorr_coeff, sequence

# Example usage:
file_path = 'converted_numbers.txt'  # Replace with the path to your text file
try:
    is_random, autocorr_coeff, sequence = autocorrelation_test_from_file(file_path)
    print("Does the sequence pass the Autocorrelation Test?", is_random)
    print("Autocorrelation coefficient:", autocorr_coeff)

    # Plot the point graph
    plt.figure(figsize=(8, 6))
    plt.plot(sequence, marker='o', linestyle='-')
    plt.title('Sequence of Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
