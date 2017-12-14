def problem_1():
    data = open('1/input_1.txt', 'r')
    numbers = data.read()
    tmp, *tail = numbers

    if numbers[-1] == numbers[0]:
        result1 = int(numbers[-1])
    else:
        result1 = 0

    for num in tail:
        if tmp == num:
            result1 += int(tmp)
        tmp = num

    result2= 0
    for i in range(len(numbers) // 2):
        if numbers[i] == numbers[i + len(numbers) // 2]:
            result2 += 2 * int(numbers[i])

    
    return result1, result2

print(problem_1())
