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

    return degrees, minutes, seconds


def DDMMSStoDecimal(degrees, minutes, seconds):
    """
    Convert degrees, minutes, seconds to decimal degrees.
    """
    return degrees + (minutes / 60.0) + (seconds / 3600.0)


def convert_file(input_filename, output_filename):
    """
    Reads angles from the input file, converts to decimal degrees,
    and writes to the output file.
    """
    with open(input_filename, 'r') as f_in, open(output_filename, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            degrees, minutes, seconds = ParseDegreeString(line)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            f_out.write(f"{decimal_degrees:.6f}\n")
