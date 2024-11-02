def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(2, False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, "cat", True]
values_dict = {"a": 2, "b": "dog", "c": False}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)