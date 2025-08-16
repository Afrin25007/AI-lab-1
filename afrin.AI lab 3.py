from itertools import permutations

def solve_cryptarithmetic(puzzle):
    term1, term2, result = puzzle
    unique_chars = sorted(set(char for word in puzzle for char in word if char.isalpha()))

    for digits in permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, digits))

        if any(char_to_digit[word[0]] == 0 for word in [term1, term2, result]):
            continue

        num1 = int("".join(str(char_to_digit[char]) for char in term1))
        num2 = int("".join(str(char_to_digit[char]) for char in term2))
        num_result = int("".join(str(char_to_digit[char]) for char in result))

        if num1 + num2 == num_result:
            return char_to_digit

    return None

if __name__ == "__main__":
    puzzle = ('CAR', 'BUS', 'TRUCK')
    solution = solve_cryptarithmetic(puzzle)

    if solution:
        print("Solution found:")
        for word in puzzle:
            print("".join(str(solution[char]) for char in word), end=" ")
        print()
    else:
        print("No solution found.")
        print("Afrin.u  B.Tech AIDS")
