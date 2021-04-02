i = 0
for k in range(0, 1000):
    if k % 3 == 0 or k % 5 == 0:
        i += k
    else:
        continue
print(i)