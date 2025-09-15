height = int(input("Enter maximum height: "))

# Print the increasing part
for i in range(1, height + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Print the decreasing part
for i in range(height - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()