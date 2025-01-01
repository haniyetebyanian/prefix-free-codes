# DM finally Project by Zeynab Golchin & Haniye Tebyanian 

def partition_string (string, current = []) :
    if not string :
        return [current]

    save_current = []
    for i in range(1, len(string) + 1) :
        prefix = string[:i] 
        supplement = string[i:]

        if len(prefix) <= 3 :
            save_current.extend(partition_string(supplement, current + [prefix]))

    return save_current        
            




binary = "0101010"
out = partition_string(binary)     
for i in out :
    print(i)  
#print(out) 

