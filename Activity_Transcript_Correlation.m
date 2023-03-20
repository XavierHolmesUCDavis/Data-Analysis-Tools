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
