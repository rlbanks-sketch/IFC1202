# Constants
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR
SECONDS_IN_YEAR = 365 * SECONDS_IN_DAY

# Prompt user for input
total_seconds = int(input("Enter length of time in seconds: "))

# Calculate years
years = total_seconds // SECONDS_IN_YEAR
remaining_seconds = total_seconds % SECONDS_IN_YEAR

# Calculate days
days = remaining_seconds // SECONDS_IN_DAY
remaining_seconds = remaining_seconds % SECONDS_IN_DAY

# Calculate hours
hours = remaining_seconds // SECONDS_IN_HOUR
remaining_seconds = remaining_seconds % SECONDS_IN_HOUR

# Calculate minutes
minutes = remaining_seconds // SECONDS_IN_MINUTE
remaining_seconds = remaining_seconds % SECONDS_IN_MINUTE

# Remaining seconds
seconds = remaining_seconds

# Print results
print(f"Years: {years}")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")