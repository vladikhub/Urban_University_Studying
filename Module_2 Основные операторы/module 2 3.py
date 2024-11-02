nums = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while True:
    if index == len(nums) or nums[index] < 0:
        break
    if nums[index] == 0:
        index += 1
        continue
    print(nums[index])
    index += 1
