rule sort_files_per_experiment:
    input:
        "Experiment_CSVs/{csv_file}.csv"
    output:
        directory("File_Sorting/Individual_Files/{csv_file}")
    conda:
        "../envs/glycomics_new.yml"
    shell:
        "python workflow/scripts/sort_csvs.py {input} {output}"