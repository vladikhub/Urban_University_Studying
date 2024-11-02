def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string: str, list_to_search: list):
    count_calls()
    for i in range(len(list_to_search)):
        if isinstance(list_to_search[i], str):
            list_to_search[i] = list_to_search[i].lower()
    return string.lower() in list_to_search

calls = 0

print(string_info("Ежик"))
print(is_contains("hah", [1, True, "Hah"]))
print(string_info("Help"))
print(is_contains("cat", [2, "god"]))
print(string_info("ручКа"))

print(calls)