jumlah_lawan = 0
kemahiran_lawan = 0
kemahiran_didapat = 0
is_valid_input = False
jumlah_lawan = 0
kemahiran = 0

while not is_valid_input:
    jumlah_lawan_dan_kemahiran = input("Jumlah lawan dan kemahiran: ").split()
    kemahiran_lawan = input("Kemahiran lawan: ").split()
    kemahiran_didapat = input("Kemahiran didapat: ").split()
    
    jumlah_lawan = int(jumlah_lawan_dan_kemahiran[0])
    kemahiran = int(jumlah_lawan_dan_kemahiran[1])
    
    if jumlah_lawan != len(kemahiran_lawan):
        print("Invalid input: Kemahiran lawan tidak sesuai dengan jumlah lawan")
        is_valid_input = False
    elif jumlah_lawan != len(kemahiran_didapat):
        print("Invalid input: Kemahiran didapat tidak sesuai dengan jumlah lawan")
        is_valid_input = False
    else:
        is_valid_input = True
        
    if not is_valid_input:
        is_retry = input("Retry? (y/n): ")
        if is_retry == "n":
            quit()

dict_kemahiran_lawan = {}
for i in range(jumlah_lawan):
    dict_kemahiran_lawan[int(kemahiran_lawan[i])] = int(kemahiran_didapat[i])


# Sort Dictionary
dict_keys = list(dict_kemahiran_lawan.keys())
dict_keys.sort()

sorted_dict_kemahiran_lawan = {i: dict_kemahiran_lawan[i] for i in dict_keys}

for key in sorted_dict_kemahiran_lawan:
    if kemahiran >= key:
        kemahiran += sorted_dict_kemahiran_lawan[key]
        
print("Kemahiran akhir: ", kemahiran)