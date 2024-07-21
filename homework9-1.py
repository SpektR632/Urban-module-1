def apply_all_func(int_list,*function):
    func_result = {}
    for func in function:
        func_result[func.__name__] = func(int_list)
    return func_result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
