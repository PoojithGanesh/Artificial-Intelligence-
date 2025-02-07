from itertools import permutations

def solve_cryptarithm():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        S, E, N, D, M, O, R, Y = mapping['S'], mapping['E'], mapping['N'], mapping['D'], mapping['M'], mapping['O'], mapping['R'], mapping['Y']
        
        # Ensure no leading zeros
        if S == 0 or M == 0:
            continue
        
        send = S * 1000 + E * 100 + N * 10 + D
        more = M * 1000 + O * 100 + R * 10 + E
        money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
        
        if send + more == money:
            print(f"Solution found: {mapping}")
            return
    print("No solution found.")

solve_cryptarithm()


# output
# Solution found: {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}
