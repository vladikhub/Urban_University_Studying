first = int(input())
second = int(input())
third = int(input())
# if first == second == third:
#     print(3)
# elif first == second or second == third or first == third:
#     print(2)
# else:
#     print(0)
set_ = {first, second, third}
if len(set_) == 1:
    print(3)
elif len(set_) == 2:
    print(2)
else:
    print(0)