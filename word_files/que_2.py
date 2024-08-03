array = list (map ( int,input().split() ))
min = abs (array[0]+array[1])
for i in range (0,len(array)):
    for j in range (i+1,len(array)):
        temp = array[i]+ array[j]
        if abs(temp) < min :
            min = abs(temp)

for i in range (0,len(array)):
    for j in range (i+1,len(array)):
        temp = array[i]+ array[j]
        if abs(temp) == min :
            print(array[i],array[j])