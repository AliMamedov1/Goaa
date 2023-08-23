my_name = ["a","l","i","m","a","m","e","d","o","v","i"]
i = 0
tanxmovnebi = 0


while i < len(my_name):
    char = my_name[i]   
    if char != "a" and char != "i" and char != "e" and char != "o" and char != "i" and char != "u":
        tanxmovnebi = tanxmovnebi + 1
    i = i+1  


print(tanxmovnebi)