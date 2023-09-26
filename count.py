
from string import ascii_lowercase




veta = input("Zadejte větu: ")
letters = dict()
character_count = 0


    
for i in ascii_lowercase:
    letters[i] = 0

for character in veta:
    if character not in letters.keys():
        letters[character] = 1
    else:
        letters[character] += 1
    character_count += 1
    

for key, value in letters.items():
    print(f"{key} : {value} {round(value * (100/character_count), 1)}% {'#' * int((int(round(value * (100/character_count), 0))) * 0.5)} ")