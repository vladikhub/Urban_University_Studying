#
#
# def gen_repeat(n):
#     def repeat(s):
#         return (s[:2] + '-') * n + s
#     return repeat
#
# s_list = ['кот', 'сова', 'орангутанг']
# rep_list = [gen_repeat(x) for x in range(1, 4)]
#
# res = [func(animal) for animal in s_list for func in rep_list]
#
# print(res)
# rep3 = gen_repeat(2)
# rep5 = gen_repeat(10)
#
# print(rep3('мишка'))
# print(rep5('фифа'))




def memorize_func(f):
    mem_res = {}

    def wrapper(a, b):
        if (a, b) not in mem_res:
            mem_res[(a, b)] = f(a, b)

        return mem_res[(a, b)]

    return wrapper

@memorize_func
def func(a, b):
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')