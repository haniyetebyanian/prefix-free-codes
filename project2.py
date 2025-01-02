# DM finally Project by Zeynab Golchin & Haniye Tebyanian 

def partition_string (string, current = []) :
    
    stack = [(string, [])]
    results = []

    while stack:
        remaining, current = stack.pop()

        if not remaining:
            results.append(current)
            continue
        for i in range(1, len(remaining) + 1) :
            prefix = remaining[:i]
            if len(prefix) <= 3 :
                stack.append((remaining[i:], current + [prefix]))

    unique = []
    for row in results :
        array_row = list(set(row))
        unique.append(array_row)

    final= []
    for row in unique :
        condition = 1
        for i in range(len(row)):
            for j in range(i + 1,len(row)) :
                if  ((str(row[j]).startswith(str(row[i]))) or (str(row[i]).startswith(str(row[j])))) :
                    condition = condition * 0

        if condition == 1 :
            final.append(row)                
        

    return final        
            

binary = input()
partition_output = partition_string(binary)


desired_state = 0
english_character_number = 26
sum = 1
for row in partition_output :
    #print(row)
    
    for letter in range(len(row)) :
        sum = sum * english_character_number
        english_character_number = english_character_number - 1
    desired_state = desired_state + sum
    
    sum = 1
    english_character_number = 26

print(len(partition_output) % 1000000007)    
print(desired_state % 1000000007)        
