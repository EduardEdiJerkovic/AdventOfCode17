def problem_2():
    data = open('2/input_2.txt', 'r')
    result1 = 0
    result2 = 0
    for line in data:
        #print(line.split())
        result1 += minmax_difference(line.split())

    data.close()
    data = open('2/input_2.txt', 'r')
    for line in data:
        result2 += devision(line.split())

    return result1, result2

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

def devision(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if int(numbers[i]) // int(numbers[j]) == int(numbers[i]) / int(numbers[j]):
                #print('1', int(numbers[i]) // int(numbers[j]))
                return int(numbers[i]) // int(numbers[j])
            elif int(numbers[j]) // int(numbers[i]) == int(numbers[j]) / int(numbers[i]):
                #print('2', int(numbers[j]) // int(numbers[i]))
                return int(numbers[j]) // int(numbers[i])

    print('Bad line.')
print(problem_2())
