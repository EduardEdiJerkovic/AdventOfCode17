def problem_5():
    data = open('5/input_5.txt', 'r')
    maze = {}
    count = 0
    for line in data:
        maze[count] = int(line)
        count += 1

    index = 0
    steps = 0
    while index in maze:
        maze[index] += 1
        index += maze[index] - 1
        steps += 1
    
    return steps
 
print(problem_5())
