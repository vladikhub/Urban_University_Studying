n = int(input())
ans = []
for i in range(1, n):
    for j in range(1, n):
        if n % (i+j) == 0 and [i, j] not in ans and [j, i] not in ans and i != j:
            ans.append([i, j])
for i in ans:
    print(''.join(map(str, i)), end='')
