def all_variants(text):
    count = 0
    for i in range(len(text)):
        for j in range(len(text)-count):
            yield text[j:j+count+1]
        count += 1

a = all_variants("морковь")
for i in a:
    print(i)
