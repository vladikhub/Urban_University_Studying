data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    ans = 0
    if len(args) == 0:
        return 0
    if len(args) == 1:
        if isinstance(args[0], int):
            return args[0]
        if isinstance(args[0], str):
            return len(args[0])
    for i in args:
        if isinstance(i, list):
            ans += calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            ans += calculate_structure_sum(*i)
        elif isinstance(i, set):
            ans += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            arr = list(i.items())
            ans += calculate_structure_sum(*arr)
        elif isinstance(i, int) or isinstance(i, str):
            ans += calculate_structure_sum(i)
    return ans


result = calculate_structure_sum(data_structure)
print(result)
