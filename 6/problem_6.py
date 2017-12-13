def problem_6():
    data = open('6/input_6.txt', 'r')
    blockes = [int(x) for x in data.readline().split()]
    dictionary = {}
    length = len(blockes)
    steps = 0
    
    while tuple(blockes) not in dictionary:
        dictionary[tuple(blockes)] = steps    

        max_value = max(blockes) 
        index = blockes.index(max(blockes))

        increment = max_value // length

        blockes[index] = 0
        for i in range(length):
            blockes[i] += increment

        excess = max_value - length * increment

        for i in range(1, excess + 1):
            if index + i < length:
                blockes[index + i] += 1
            else:
                blockes[index + i - length] += 1

        steps += 1
        
    return (steps, steps - dictionary[tuple(blockes)])

print(problem_6())
    