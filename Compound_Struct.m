% open the file
fid = fopen('Test.csv');

% initialize the compound struct
compound = struct();

% read the file line by line
tline = fgetl(fid);
while ischar(tline)
    % if the line contains the string 'Cpd', this is the start of a new compound
    if contains(tline, 'Cpd')
        % extract the compound number from the line
        c_num = extractBetween(tline, 'Cpd ', ':');
        c_num = str2double(c_num{1});

        % read the next line to skip the headers
        fgetl(fid);

        % read the data for this compound using textscan
        data = textscan(fid, '%f%f%f', 'Delimiter', ',');

        % create a struct for this compound
        compound(c_num).Points = data{1};
        compound(c_num).X_Minutes = data{2};
        compound(c_num).Y_Counts = data{3};

        % print a message indicating which compound has been stored in the struct
        fprintf('Compound %d stored in struct\n', c_num);
    end
    
    % read the next line
    tline = fgetl(fid);
end

% close the file
fclose(fid);

% plot the X and Y values for each compound on a single plot
figure;
hold on;
for i = 1:numel(compound)
    x_vals = compound(i).X_Minutes;
    y_vals = compound(i).Y_Counts;
    plot(x_vals, y_vals, '-o', 'DisplayName', sprintf('Compound %d', i));
end
hold off;
legend('Location', 'best');
xlabel('X (Minutes)');
ylabel('Y (Counts)');
title('X vs Y for each Compound');
