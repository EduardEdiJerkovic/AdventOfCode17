def problem_2():
    data = open('2/input_2.txt', 'r')
    result = 0
    for line in data:
        #print(line.split())
        result += minmax_difference(line.split())

    return result

def minmax_difference(numbers):
    #print(numbers[0])
    min_num = int(numbers[0])
    max_num = int(numbers[0])
    for num in numbers:
        if int(num) < min_num:
            min_num = int(num)
        if int(num) > max_num:
            max_num = int(num)
    return max_num - min_num

print(problem_2())
