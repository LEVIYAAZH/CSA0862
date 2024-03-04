def letter_combinations(digits):
    if not digits:
        return []

    digit_letters_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            combinations.append(combination)
        else:
            for letter in digit_letters_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    combinations = []
    backtrack('', digits)
    return combinations

# Get input from the user
digits = input("Enter the digits (e.g., '23'): ")

# Call the function with user input
print(letter_combinations(digits))
