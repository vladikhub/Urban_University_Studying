def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    cur = int(str_number[0])
    return cur * get_multiplied_digits(int(str_number[1::]))


result = get_multiplied_digits(234)
print(result)