from pprint import pprint
import inspect


class Test:
    def __init__(self, name, word):
        self.__name = name
        self.word = word

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    def hello(self):
        print(f"{self.__name} сказал '{self.word}'")


def introspection_info(obj):

    attrs = [item for item in dir(obj) if not callable(getattr(obj, item)) and not item.startswith('__')]

    meths = list(filter(lambda x: x not in attrs, dir(obj)))
    info = {
        'type': type(obj),
        'attributes': attrs,
        'methods': meths,
        'module': inspect.getmodule(obj),
        'class_name': obj.__class__.__name__
            }

    return info


test = Test("Влад", 'Я тестируюсь')
pprint(introspection_info(test))

