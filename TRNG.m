% Load the .mat file
load('test.mat');

% Convert decimal values to strings
decimal_strings = arrayfun(@num2str, out.simout.Data, 'UniformOutput', false);

% Initialize cell array to store concatenated strings
concatenated_strings = {};
batch_size = 1;
num_batches = ceil(length(decimal_strings) / batch_size);

% Initialize cell arrays to store original numbers, hashed seeds, and converted numbers
original_numbers = {};
hashed_seeds = {};
converted_numbers = {};

for i = 1:num_batches
    start_index = (i - 1) * batch_size + 1;
    end_index = min(i * batch_size, length(decimal_strings));
    
    batch_decimal_strings = decimal_strings(start_index:end_index);
    
    % Concatenate decimal strings in this batch
    concatenated_string = strjoin(batch_decimal_strings, '');
    
    % Store concatenated string
    concatenated_strings{i} = concatenated_string;
    
    % Store original numbers
    original_numbers{i} = str2double(batch_decimal_strings); % Convert strings back to numbers
    
    % Hash each concatenated string using SHA-256 algorithm
    hashed_seed = generateSHA256(concatenated_strings{i});
    hashed_seeds{i} = hashed_seed;
    
    % Convert hashed seed to a number between 0 and 1
    num = hex2num(hashed_seed);
    converted_numbers{i} = num;
end

% Display the original numbers, hashed seeds, and converted numbers nicely in a table
disp('Original Numbers, Hashed Seeds, and Converted Numbers:');
disp('--------------------------------------------------------------------------------------------------');
disp('Batch   | Original Numbers       | Hashed Seed               | Converted Number');
disp('--------------------------------------------------------------------------------------------------');
for i = 1:num_batches
    disp([sprintf('%5d', i), '   |   ', num2str(original_numbers{i}), '   |   ', hashed_seeds{i}, '   |   ', num2str(converted_numbers{i})]);
end
disp('--------------------------------------------------------------------------------------------------');

% Extract converted numbers from the cell array
all_converted_numbers = cell2mat(converted_numbers);

% Plot histogram
figure;
histogram(all_converted_numbers, 'Normalization', 'probability');
title('Histogram of TRNG');
xlabel('Converted Number');
ylabel('Probability');

% Specify the file name
txt_file_name = 'converted_numbers.txt';

% Write the converted numbers to a text file
dlmwrite(txt_file_name, all_converted_numbers, 'delimiter', '\n');
disp(['Converted numbers have been exported to ', txt_file_name]);

function hash = generateSHA256(inputString)
    % Convert MATLAB string to Java string
    javaString = java.lang.String(inputString);
    
    % Get the SHA-256 digest instance
    digest = java.security.MessageDigest.getInstance('SHA-256');
    
    % Compute the digest
    digestBytes = digest.digest(javaString.getBytes());
    
    % Convert bytes to hexadecimal string
    hash = reshape(dec2hex(typecast(digestBytes, 'uint8'))', 1, []);
end

function num = hex2num(hexString)
    % Convert hexadecimal string to a number between 0 and 1
    num = 0;
    for i = 1:length(hexString)
        num = num * 16 + hex2dec(hexString(i));
    end
    num = num / 16^length(hexString);
end
