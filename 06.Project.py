def merge_files(input_filename, merge_filename, output_filename):
    input_records = 0
    merge_records = 0
    output_records = 0
    merge_inserted = False

    with open(output_filename, 'w') as outfile, open(input_filename, 'r') as infile:
        for line in infile:
            if not merge_inserted :
                # Write the line containing the marker
                outfile.write(line)
                output_records += 1

                # Insert contents of merge file here
                with open(merge_filename, 'r') as mergefile:
                    for merge_line in mergefile:
                        outfile.write(merge_line)
                        merge_records += 1
                        output_records += 1
                merge_inserted = True
            else:
                # Just copy line from input to output
                outfile.write(line)
                input_records += 1
                output_records += 1

    print(f"Number of records in input file: {input_records}")
    print(f"Number of records in merge file: {merge_records}")
    print(f"Number of records in output file: {output_records}")


# File names as per your request
input_file = "06.Project Input File.txt"
merge_file = "06.Project Merge File.txt"
output_file = "06.Project Output File.txt"

merge_files(input_file, merge_file, output_file)
