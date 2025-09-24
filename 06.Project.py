def merge_files():
    input_filename = "06.Project Input File.txt"
    merge_filename = "06.Project Merge File.txt"
    output_filename = "06.Project Output File.txt"

    input_count = 0
    merge_count = 0
    output_count = 0

    # Open output file for writing
    with open(output_filename, 'w') as outfile:
        # Open input file for reading
        with open(input_filename, 'r') as infile:
            for line in infile:
                stripped_line = line.rstrip('\n')
                if stripped_line == "**Insert Merge File Here**":
                    # Instead of writing the marker, we read and write merge file contents
                    with open(merge_filename, 'r') as mergefile:
                        for mline in mergefile:
                            outfile.write(mline)
                            merge_count +=1
                            output_count +=1
                    # Do not write the marker line itself
                    continue
                else:
                    outfile.write(line)
                    input_count +=1
                    output_count +=1

    print(f"{input_count} input file records")
    print(f"{merge_count} merge file records")
    print(f"{output_count} output file records")


if __name__ == "__main__":
    merge_files()
