# Initialize the list to hold all property data
properties = []

# Step 1: Open the file, read each line, split, convert price, and append to properties list
with open("Exam Two Properties.csv", "r") as file:
    # If there's a header, read and skip it
    header = file.readline()
    
    for line in file:
        line = line.strip()  # Remove trailing newline
        data = line.split(",")  # Split by comma
        
        # Convert price (column 4) to float
        data[4] = float(data[4])
        
        # Append this list to properties
        properties.append(data)

# Step 2: Print the headings and then print the two-dimensional properties list
print(f"{'Address':<30} {'City':<15} {'State':<7} {'Zip Code':<10} {'Price':>12}")
print("-" * 80)
for prop in properties:
    print(f"{prop[0]:<30} {prop[1]:<15} {prop[2]:<7} {prop[3]:<10} ${prop[4]:>11,.2f}")

# Step 3: Create an empty two-dimensional list zipcodes
zipcodes = []

# Step 4: Loop through all rows in properties
for prop in properties:
    zipcode = prop[3]
    price = prop[4]
    
    # Step 5: Loop through rows in zipcodes to find if the zipcode already exists
    found = False
    for z in zipcodes:
        if z[0] == zipcode:
            # Zipcode match found
            z[1] += 1  # Increment count
            z[2] += price  # Add price to sum
            found = True
            break
    
    # Step 6: If no match in zipcodes list, append new row
    if not found:
        zipcodes.append([zipcode, 1, price])

# Step 7: Print the headings of the report
print("\nZip Code Summary Report")
print(f"{'Zip Code':<10} {'Count':>8} {'Avg Price':>15}")
print("-" * 37)

# Step 8: Loop through zipcodes and print Zipcode, Count, and Average Price
for z in zipcodes:
    zipcode = z[0]
    count = z[1]
    sum_prices = z[2]
    avg_price = sum_prices / count
    
    print(f"{zipcode:<10} {count:>8} ${avg_price:>14,.2f}")
