def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(4, 'строчки')
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [6, 'шесть', False]
value_dict = {}
value_dict['4'] = 'четыре'
value_dict['стр'] = 2
value_dict['True'] = [4, 5, 6]
print_params(*values_list)

print_params(*value_dict) #Почему-то не распаковывает словарь с двумя ** -
# TypeError: print_params() got an unexpected keyword argument '4'

values_list_2 = [False, 'Ложь']
print_params(*values_list_2, 42)


