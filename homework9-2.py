first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [i for i in first_strings if len(i) >= 5]
print(first_result)
second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
print(second_result)
third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}
print(third_result)
