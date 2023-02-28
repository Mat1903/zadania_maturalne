file = open("liczby.txt")
line = int(file.readline())

def sum_of_numbers(n):
    sum = 0
    for i in n:
        sum += i

    return sum

result = []

for line in file:
    lineog = [line.rstrip()]
    while len(line) != 1:
        line = [sum_of_numbers(line.rstrip())]
        if sum_of_numbers(line) == 1:
            result.append(lineog)
            break











