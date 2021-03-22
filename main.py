

for i in range(1,100000,2):
    counter = 0
    for a in range(1,i):
        if counter >=2:
            break
        elif i % a == 0:
            counter+=1
    if counter <= 1:
        print("{} is a prime number".format(i))
