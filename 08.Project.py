def main():
    # Open and read the file constitution.txt with linefeed stripped
    with open('constitution.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    while True:
        search_term = input("Enter search term: ").strip()
        if not search_term:
            break  # exit on blank input

        i = 0
        n = len(lines)
        while i < n:
            if search_term.lower() in lines[i].lower():
                # Find start of section by moving backward until blank line or start of file
                start = i
                while start > 0 and lines[start].strip() != '':
                    start -= 1
                if lines[start].strip() == '':
                    start += 1  # move forward to first non-blank line

                # Find end of section by moving forward until blank line or end of file
                end = i
                while end < n and lines[end].strip() != '':
                    end += 1

                # Print section with line numbers
                for line_num in range(start, end):
                    print(f"Line {line_num}: {lines[line_num]}")
                print()  # blank line after section

                i = end  # skip past this section
            else:
                i += 1

if __name__ == "__main__":
    main()
