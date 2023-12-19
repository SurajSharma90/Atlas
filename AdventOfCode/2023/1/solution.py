try:
    file = open("input.txt", "r")

    sum = 0
    for line in file:
        for s in line:
            if s.isdigit():
                sum += int(s)
                break
    
    print(sum)

except Exception as e:
    print(e)


