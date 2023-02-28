file = open("liczby.txt")
line = int(file.readline())


def first_number(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
            break
        d += 1
        if n < 2:
            return False
            break
        else:
            return True
            break

result = []

for line in file:
    linereversed = line[::-1]
    if first_number(int(linereversed)) == True:
        result.append(line.rstrip())

print(result)