def ParseDegreeString(ddmmss):
    """
    Parse a string in the form dd°mm'ss" and return degrees, minutes, seconds as floats.
    """
    degree_sym = chr(176)  # °
    deg_pos = ddmmss.find(degree_sym)
    min_pos = ddmmss.find("'")
    sec_pos = ddmmss.find('"')

    degrees = float(ddmmss[:deg_pos])
    minutes = float(ddmmss[deg_pos+1:min_pos])
    seconds = float(ddmmss[min_pos+1:sec_pos])
    
    # Normalize: if seconds == 60, increment minutes and set seconds to 0
    if seconds == 60:
        seconds = 0
        minutes += 1
        
    # Normalize: if minutes == 60, increment degrees and set minutes to 0
    if minutes == 60:
        minutes = 0
        degrees += 1
    
    return degrees, minutes, seconds


def DDMMSStoDecimal(degrees, minutes, seconds):
    """
    Convert degrees, minutes, seconds to decimal degrees.
    """
    return degrees + (minutes / 60.0) + (seconds / 3600.0)


def main():
    input_file = "07.Project Angles Input.txt"
    output_file = "07.Project Angles Output.txt"
    
    count = 0
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue  # skip empty lines
                
            degrees, minutes, seconds = ParseDegreeString(line)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            f_out.write(f"{decimal_degrees}\n")
            count += 1

    print(f"{count} records processed")


if __name__ == "__main__":
    main()
