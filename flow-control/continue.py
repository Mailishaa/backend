stop= int (input ("Enter the counter stop: "))
count = 1
while count <= stop:
    if count %2==0:
        count+=1
        continue
    print(count)
    count+=1
