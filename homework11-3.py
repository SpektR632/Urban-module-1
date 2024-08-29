import inspect


def introspection_info(obj):
    info = {'type': str(type(obj)).split()[1][1:-2], 'attributes': [i for i in dir(obj) if not '__' in i],
            'methods': [i for i in dir(obj) if '__' in i],
            'module': str(inspect.getmodule(obj, 'homework11-3.py')).split()[1][1:-1]}
    return info


number_info = introspection_info(42)
print(number_info)
