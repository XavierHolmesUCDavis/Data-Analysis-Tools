%% Convert glycan abundance data to percent type
% Define the path to the CSV_Data folder
folder_path = '\Users\xavie\OneDrive\Documents\GitHub Repositories\Data-Analysis-Tools\CSV_Data';

% Get a list of all CSV files in the folder
file_list = dir(fullfile(folder_path, '*.csv'));

% Loop through each file in the list
for i = 1:numel(file_list)
        % Get the name of the current file
    file_name = file_list(i).name;
    
    % Read in the table
    data = readtable(fullfile(folder_path, file_name));
% extract the sample names from the headers of the table
sample_names = data.Properties.VariableNames(7:end);

% initialize a cell array to store the percentages for each sample
percentages = cell(length(sample_names), 6);

% loop through each sample
    for j = 1:length(sample_names)
    
        % extract the numerical data for the current sample
        sample_data = table2array(data(:, 6+j));
    
        % initialize counters for each percentage value
        hm_count = 0;
        undec_count = 0;
        fuc_count = 0;
        sia_count = 0;
        sifuc_count = 0;
    
        % loop through each row of the sample data and update the counters
        for k = 1:length(sample_data)
        
            % extract the class string for the current row
            class_str = data.Class{k};
        
            % check if the class is high mannose
            if strcmpi(class_str, 'HM')
                hm_count = hm_count + sample_data(k);
            % check if the class is undecorated
            elseif isempty(strfind(class_str, 'F')) && isempty(strfind(class_str, 'S'))
                undec_count = undec_count + sample_data(k);
            % check if the class is fucosylated
            elseif ~isempty(strfind(class_str, 'F')) && isempty(strfind(class_str, 'S'))
                fuc_count = fuc_count + sample_data(k);
            % check if the class is sialylated
            elseif ~isempty(strfind(class_str, 'S')) && isempty(strfind(class_str, 'F'))
                sia_count = sia_count + sample_data(k);
            % check if the class is sialofucosylated
            elseif ~isempty(strfind(class_str, 'F')) && ~isempty(strfind(class_str, 'S'))
                sifuc_count = sifuc_count + sample_data(k);
            end
        
        end
            
    % calculate the percentages for the current sample and store them in the cell array
    total = sum(sample_data);
    percentages{j, 1} = sample_names{j};
    percentages{j, 2} = hm_count;
    percentages{j, 3} = undec_count; 
    percentages{j, 4} = fuc_count;
    percentages{j, 5} = sia_count;
    percentages{j, 6} = sifuc_count;
    
    end

% create a table from the cell array of percentages
percentages_table = cell2table(percentages, 'VariableNames', {'Sample', 'High_Mannose', 'Undecorated', 'Fucosylated', 'Sialylated', 'Sialofucosylated'});

% get the input filename without the extension
filename = file_list(i).name;
[~, name, ~] = fileparts(filename);

% create the output filename
output_filename = strcat(name, '_percentages.csv');

% write the table to a csv file
writetable(percentages_table, output_filename);

% print message indicating that the percentages have been written to the file
fprintf('Percentages written to %s\n', output_filename);

% Read in the table
data = readtable(output_filename);

% Transpose the table
data = rows2vars(data);

% Get the new header row
new_header = data.Properties.RowNames';

% Replace the first element of the first row with 'Class'
data.Properties.VariableNames{1} = 'Class';
data.Class{1} = 'Class';
export_csv_name = strcat(name, '_percentages_GraphPad.csv');

% write the table to a csv file
writetable(data, export_csv_name);
    
end

disp('Corresponding files are ready for export to GraphPad')
