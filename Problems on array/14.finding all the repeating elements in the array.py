def finding_repeating(arr):
    frequency = {}
    repeating_elements = []

    # Count the frequency of each element
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find elements with frequency greater than 1
    for key, value in frequency.items():
        if value > 1:
            repeating_elements.append(key)

    return repeating_elements

# Test Examples
arr1 = [1, 1, 2, 3, 4, 4, 5, 2]
arr2 = [1, 1, 0]

print(finding_repeating(arr1))  # Output: [1, 2, 4]
print(finding_repeating(arr2))  # Output: [1]
