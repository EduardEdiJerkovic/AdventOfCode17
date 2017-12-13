from math import sqrt

def problem_3():
    data = open('3/input_3.txt', 'r')
    number = int(data.read())
    #print(number)
    # Every down-right square form first is potencial of odd number (1, 9, 25, 49, ...)
    layer = int(sqrt(number))
    if layer % 2 == 0:
        layer -= 1
    
    difference = number - layer ** 2

    pos = ((layer - 1) / 2, (layer - 1) / 2)

    next_layer = layer + 1

    if difference == 0:
        pass
    elif difference <= next_layer:
        pos = (pos[0] - difference + 1, pos[1] + 1)
    elif difference <= 2 * next_layer:
        pos = (pos[0] - next_layer + 1, pos[1] + 1)
        pos = (pos[0], pos[1] - (difference - next_layer))
    elif difference <= 3 * next_layer:
        pos = (pos[0] - next_layer + 1, pos[1] + 1)
        pos = (pos[0], pos[1] - next_layer)
        pos = (pos[0] + (difference - 2 * next_layer), pos[1])
    else:
        pos = (pos[0] - next_layer + 1, pos[1] + 1)
        pos = (pos[0], pos[1] - next_layer)
        pos = (pos[0] + next_layer, pos[1])
        pos = (pos[0], pos[1] + difference - 3 * next_layer)

    #print(pos)
    return (abs(pos[0]) + abs(pos[1]))

print(problem_3())
