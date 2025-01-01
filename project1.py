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
        

    return unique        
            

binary = "0101010"
out = partition_string(binary)


for i in out :
    print(i)

