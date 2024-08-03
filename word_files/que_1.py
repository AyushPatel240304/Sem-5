chef1 = []
chef2 = []
chef1score = 0
chef2score = 0
print ("_________________________________________\n")
print ("Enter the rating for two chef: ")
print ("Press 1 for Presentation ")
print ("Press 2 for taste ")
print ("Press 3 for hygiene")
print ("_________________________________________\n\n")

for i in range (3):
    chef1.append(int(input(f"Enter Chef 1's rating for {i+1}:")))
    print ("\n_________________________________________\n\n")

for i in range (3):
    chef2.append(int(input(f"Enter Chef 2's rating for {i+1}:")))
    print ("\n_________________________________________\n\n")


for i in range (3):
    if chef1[i] > chef2[i]:
        chef1score += 1

    elif chef2[i] > chef1[i]:
        chef2score += 1

print (f"Chef-1's Score is {chef1score}\n")
print (f"Chef-2's Score is {chef2score}\n")


    