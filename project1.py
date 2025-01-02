# DM finally Project by Zeynab Golchin & Haniye Tebyanian 
import numpy  as np

def partition_string (string, current = []) :
    if not string :
        return [current]

    save_current = []
    for i in range(1, len(string) + 1) :
        prefix = string[:i] 
        supplement = string[i:]

        if len(prefix) <= 3 :
            save_current.extend(partition_string(supplement, current + [prefix]))


    unique = []
    for row in save_current :
        array_row = np.array(row)
        unique.append(np.unique(array_row))

    final= []
    for row in unique :
        condition = 1
        for i in range(len(row)):
            for j in range(i + 1,len(row)) :
                if not ((str(row[j]).startswith(str(row[i]))) or (str(row[i]).startswith(str(row[j])))) :
                    condition = condition * 1
                else :
                    condition = condition * 0

        if condition == 1 :
            final.append(np.array(row))                
        

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
