rule create_compositional_files:
    input:
        "Experiment_CSVs/{wildcards.csv_file}.csv"
    output:
        directory("OutputFolder1/{wildcards.csv_file}")
    shell:
        "python workflow/scripts/compositional.py InputFolder1/{wildcards.csv_file} {output}"