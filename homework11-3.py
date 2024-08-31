import inspect


def introspection_info(object):
    info = {'type': type(object), 'attributes': object.__dir__(),
            'methods': dir(object),
            'module': inspect.getmodule(object, 'homework11-3.py')}
    return info


number_info = introspection_info(42)
print(number_info)
