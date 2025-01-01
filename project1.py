# DM finally Project by Zeynab Golchin & Haniye Tebyanian by 

def partition_string (string, current = []) :
    if not string :
        print(current)
        return

    for i in range(1, len(string) + 1) :
        prefix = string[:i] 
        supplement = string[i:]

        if len(prefix) <= 3 :
            partition_string(supplement, current + [prefix])
            




# check
binary = "0101010"
partition_string(binary)        

