import inspect

def introspection_info(object):
    info = {'type': type(object), 'attributes': [i for i in object.__dir__() if not callable(getattr(object, i))],
            'methods': dir(object),
            'module': inspect.getmodule(object, 'homework11-3.py')}
    return info


number_info = introspection_info(42)
print(number_info)

