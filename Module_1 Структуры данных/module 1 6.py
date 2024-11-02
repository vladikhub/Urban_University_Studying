my_dict = {"Влад": 2005, "Слава": 2004}
print(my_dict)
print(my_dict["Влад"])
print(my_dict.get("Steve", "Какой еще стив???"))
my_dict.update({"Daria": 2006, "Andrew": 1970})
print(my_dict.pop("Andrew"))
print(my_dict)

my_set = {1, 1, 1, "Mom", "mom", "Mom", True, True, False}
print(my_set)
my_set.update({5.5, "Слово"}) # либо .add
my_set.discard("mom")
print(my_set)