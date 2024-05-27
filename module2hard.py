numb = int(input())
result = []
for i in range(1, 21):
    for j in range(i, 21):
        if (numb == i + j or numb % (i + j) == 0) and i != j:
            result += [str(i) + str(j)]

print(numb, ' - ', *result, sep='')