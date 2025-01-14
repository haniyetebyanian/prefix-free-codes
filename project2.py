base = ['0', '1', '00', '01', '10', '11', '000', '001', '010', '011', '100', '101', '110', '111']

def find_partition(string):

    n = len(string)

    # dp = Dynamic Proogramming
    
    dp = [0] * (n + 1)
    dp[0] = [frozenset()]
    # frozenset is the set that is unchagable

    for i in range(1, n + 1):
        current_set = set()
        for length in range(1, min(4, i + 1)):
            substring = string[i - length:i]
            if substring in base:
                for p_set in dp[i - length]:
                    new_set = p_set | {substring}
                    condition = True
                    for a in new_set:
                        for b in new_set:
                            if a != b and (a.startswith(b) or b.startswith(a)):
                                condition = False
                                break
                        if not condition:
                            break
                    if condition:
                        current_set.add(frozenset(new_set))
        dp[i] = current_set

    unique_partitions = dp[n]
    return unique_partitions

def calculate_desired_state(partitions):
    MOD = 1000000007
    english_character_number = 26
    desired_state = 0

    for partition in partitions:
        sum_value = 1
        remaining_letters = english_character_number

        for _ in partition:
            sum_value = (sum_value * remaining_letters) 
            remaining_letters -= 1

        desired_state = (desired_state + sum_value) % MOD

    return desired_state

binary = input()
partitions = find_partition(binary)

num_partitions = len(partitions) % 1000000007
desired_state = calculate_desired_state(partitions)

print(num_partitions)
print(desired_state)
