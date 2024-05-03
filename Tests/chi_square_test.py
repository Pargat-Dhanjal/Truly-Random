import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

def chi_square_test_from_file(file_path, num_bins=10, alpha=0.05):
    """
    Performs a Chi-Square Test on a sequence of numbers read from a text file.

    Parameters:
    - file_path: path to the text file containing the sequence of numbers
    - num_bins: number of bins to use for the Chi-Square Test (default is 10)
    - alpha: significance level for the test (default is 0.05)

    Returns:
    - True if the sequence passes the Chi-Square Test (i.e., p-value > alpha), False otherwise.
    """

    # Read the sequence of numbers from the text file
    with open(file_path, 'r') as file:
        sequence = [float(line.strip()) for line in file.readlines()]

    # Calculate observed frequencies
    observed, bins = np.histogram(sequence, bins=num_bins)

    # Expected frequencies for a uniform distribution
    expected = np.full_like(observed, len(sequence) / num_bins)

    # Adjust the last bin to include any remaining values
    expected[-1] += len(sequence) % num_bins

    # Perform Chi-Square Test
    chi_stat, p_value = chisquare(observed, expected)

    # Plot observed and expected frequencies
    plt.figure(figsize=(8, 6))
    plt.bar(bins[:-1], observed, width=(bins[1] - bins[0]), label='Observed', color='blue', alpha=0.7)
    plt.plot(bins[:-1] + (bins[1] - bins[0]) / 2, expected, 'r--', label='Expected')
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.title('Observed vs Expected Frequencies')
    plt.legend()
    plt.show()


    print("p-value:", p_value)
    print("alpha:", alpha)
    # Check if the p-value is greater than alpha
    if p_value > alpha:
        return True
    else:
        return False

# Example usage:
file_path = 'converted_numbers.txt'  # Replace with the path to your text file
is_random = chi_square_test_from_file(file_path)
print("Does the sequence pass the Chi-Square Test?", is_random)
