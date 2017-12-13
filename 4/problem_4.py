def problem_4():
    data = open('4/input_4.txt', 'r')
    result = 0
    for line in data:
        words = line.split()
        dictionary = {}
        result += 1
        for word in words:
            if word not in dictionary:
                dictionary[word] = True
            else:
                result -= 1
                break
        
    return result
            
print(problem_4())
