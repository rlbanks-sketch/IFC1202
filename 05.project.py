def count_digits(num):
    count = 0
    temp = num
    while temp > 0:
        temp //= 10
        count += 1
    # Special case for 0 (if input is 0)
    if num == 0:
        count = 1
    return count

def is_special_number(num):
    digits = count_digits(num)
    temp = num
    sum_pow = 0
    while temp > 0:
        digit = temp % 10
        sum_pow += digit ** digits
        temp //= 10
    # Special case for 0
    if num == 0:
        sum_pow = 0 ** digits
    return sum_pow == num

# Input
start_range = int(input("Enter Start of Range: "))
end_range = int(input("Enter End of Range: "))

print(f"Special Numbers between {start_range} and {end_range}")
for i in range(start_range, end_range + 1):
    if is_special_number(i):
        print(i)