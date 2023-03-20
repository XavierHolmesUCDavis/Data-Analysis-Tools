% Prompt user for number of groups
num_groups = input('How many groups are there? ');

% Initialize cell array to store group names
group_names = cell(num_groups,1);

% Prompt user for pattern to look for in headers for each group
for i = 1:num_groups
    prompt = sprintf('Enter pattern to look for in headers for group %d: ', i);
    group_names{i} = input(prompt, 's');
end

% Import enzyme score data
enzyme_data = readtable('R_Transcript_1_EnzScore.csv');

% Initialize cell array to store enzyme score data for each group
enzyme_scores = cell(num_groups,1);

% Loop through each group
for i = 1:num_groups
    % Find columns that match pattern for current group
    col_names = enzyme_data.Properties.VariableNames;
    group_cols = contains(col_names, group_names{i});

    % Extract enzyme score data for current group
    enzyme_scores{i} = enzyme_data(:, group_cols);
end

%% Load in transcript data 
% Specify the CSV file name and read in the data
transcript_file = 'normalized_counts_data.csv';
transcript_data = readtable(transcript_file);

% Extract the headers for the samples and the gene names
sample_headers = transcript_data.Properties.VariableNames(2:end);
gene_names = transcript_data{:,1};

% Initialize a cell array to store the transcript data for each group
grouped_transcripts = cell(num_groups, 1);

% Prompt the user for each group and extract the corresponding data
for i = 1:num_groups
    % Get the group name from the user
    group_name = input(sprintf('Enter name of group %d: ', i), 's');
    
    % Find the headers that match the group name pattern
    group_headers = sample_headers(startsWith(sample_headers, group_name));
    
    % Extract the transcript data for the group
    group_data = transcript_data(:, [1 find(startsWith(sample_headers, group_name))+1]);
    
    % Add the group data to the cell array
    grouped_transcripts{i} = table2array(group_data(:, 2:end));
end

% Initialize struct to store correlation coefficients
correlations = struct();

% Loop through each group
for i = 1:num_groups
    % Get enzyme data for current group
    enzyme_group = table2array(enzyme_scores{i});
    
    % Get transcript data for current group
    transcript_group = grouped_transcripts{i};
    
    % Loop through each row of enzyme data
    for j = 1:size(enzyme_group, 1)
        % Get current enzyme row
        enzyme_row = enzyme_group(j,:);
        
        % Loop through each row of transcript data
        for k = 1:size(transcript_group, 1)
            % Get current transcript row
            transcript_row = transcript_group(k,:);
            
            % Calculate Pearson correlation coefficient
            corr_coef = corr(enzyme_row', transcript_row', 'type', 'Pearson');
            
            % Store result in struct
            correlations(i).group = group_names{i};
            correlations(i).enzyme_row{j} = enzyme_row;
            correlations(i).transcript_row{k} = transcript_row;
            correlations(i).corr_coef(j,k) = corr_coef;
        end
    end
end



