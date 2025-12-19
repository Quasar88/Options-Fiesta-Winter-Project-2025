#QUESTION - 1

def find_min_max(numbers):

    minimum = numbers[0]
    maximum = numbers[0]

    for i in range(1, len(numbers)):
        current_val = numbers[i]
        if current_val > maximum:
            maximum = current_val
        if current_val < minimum:
            minimum = current_val
        return minimum, maximum

data = [15, 3, 9]
min_val, max_val = find_min_max(data)

print("Array: ", data)
print("Minimum: ", min_val)
print("Maximum: ", max_val)


#QUESTION - 2

def is_palindrome(s):
    processed_s = ''.join(filter(str.isalnum, s)).lower()
    left = 0
    right = len(processed_s) - 1

    while left < right:
        if processed_s[left] != processed_s[right]:
            return False

        left += 1
        right -= 1
    return True

#QUESTION - 3

def find_pair_with_difference(arr, x):
    arr.sort()

    i = 0
    j = 1
    n = len(arr)

    while i < n and j < n:
        diff = arr[j] - arr[i]
        if diff == x:
            return arr[i], arr[j]
        elif diff < x:
            j += 1
        else:
            i += 1
        if i == j:
            j += 1


