stop = int(input("Enter the counter stop"))
must_stop =17
count = 1
while count<=stop:
    print(count)
    if count == must_stop:
        print("Stop Reached")
        break
    count +=1