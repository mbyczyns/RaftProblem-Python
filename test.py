from itertools import permutations

def generate_combinations(m, n, function):
    matrix = [[0] * n for _ in range(m)]
    elements = list(range(m * n))

    combination_count = 0

    all_permutations = permutations(elements)

    for permutation in all_permutations:
        for i in range(m):
            for j in range(n):
                matrix[i][j] = permutation[i * n + j]

        function(matrix)

        combination_count += 1

    print(f"Liczba stworzonych kombinacji: {combination_count}")

def print_combination(matrix):
    print(matrix)

# Przykładowe użycie
m = 2
n = 3
generate_combinations(m, n, print_combination)
