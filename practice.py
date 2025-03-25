def plus_one(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # Set current digit to 0 and continue
    
    # If all digits were 9 (e.g., 999 → 1000), add a new leading 1
    return [1] + digits

# Example Test Cases
print(plus_one([1, 2, 3]))    # Output: [1, 2, 4]
print(plus_one([9, 9, 9]))    # Output: [1, 0, 0, 0]