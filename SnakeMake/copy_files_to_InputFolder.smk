rule copy_files_to_InputFolder:
    input:
        "File_Sorting/Individual_Files/{csv_file}"
    output:
        directory("InputFolder1/{csv_file}")
    shell:
        """
        mkdir -p {output}
        cp -r {input}/* {output}
        cd ../../
        """