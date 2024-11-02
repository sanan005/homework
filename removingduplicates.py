#Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
uniquenums = []
for x in nums:
    if x not in uniquenums:
        uniquenums.append(x)

print(uniquenums)