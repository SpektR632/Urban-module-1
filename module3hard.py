def calculate_structure_sum(data_structure):
    sum = 0

    if isinstance(data_structure, int):
        sum += data_structure
    elif isinstance(data_structure, str):
        sum += len(data_structure)
    elif isinstance(data_structure, list) and len(data_structure) > 0:
        for z in data_structure:
            sum += calculate_structure_sum(z)
    elif isinstance(data_structure, dict) and len(data_structure) > 0:
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
    elif isinstance(data_structure, set) and len(data_structure) > 0:
        for z in list(data_structure):
            sum += calculate_structure_sum(z)
    elif isinstance(data_structure, tuple) and len(data_structure) > 0:
        for z in data_structure:
            sum += calculate_structure_sum(z)
    return sum



data_structure = [[1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))

