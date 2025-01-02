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
        for i in range(len(row) - 1):
            for j in range(i + 1 , len(row)) :
                if not ((str(row[j]).startswith(str(row[i]))) or (str(row[i]).startswith(str(row[j])))) :
                    condition = condition * 1
                else :
                    condition = condition * 0

        if condition == 1 :
            final.append(np.array(row))                
        

    return final        
            

binary = "01110"
out = partition_string(binary)




for i in out :
    print(i)

