def problem_1():
    data = open('1/input_1.txt', 'r')
    numbers = data.read()
    tmp, *tail = numbers

    if numbers[-1] == numbers[0]:
        result = int(numbers[-1])
    else:
        result = 0

    for num in tail:
        if tmp == num:
            result += int(tmp)
        tmp = num
    
    return result

print(problem_1())
