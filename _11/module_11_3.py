def introspection_info(obj):
    attributes =[attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__module__
    info = {'type': type(obj),
            'attributes': attributes,
            'methods': methods,
            'module': module,
            }
    return info

class Planet():
    def __init__(self, color):
        self.color = color

    def func(self):
        pass


Neptune = Planet('blue',)
Neptune.__dict__['satellites'] = 16

inf = introspection_info(Neptune)
print(inf)

