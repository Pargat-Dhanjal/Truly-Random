% Generate 71977 random numbers
all_converted_numbers = rand(1, 71977);

% Plot histogram
figure;
histogram(all_converted_numbers, 'Normalization', 'probability');
title('Histogram of PRNG');
xlabel('Converted Number');
ylabel('Probability');
