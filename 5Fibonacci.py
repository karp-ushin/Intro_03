k = 8
fib_list = [0]
if k == 0:
    print(fib_list)
else:
    fib_list = [1, 0, 1]
    a = 0
    b = 1
    for i in range(2, k+1):
        fib_list.append(a + b)
        a, b = b, a + b
    a = 1
    b = 0
    for i in range(2, k+1):
        fib_list.insert(0, b-a)
        a, b = b - a, a
print(fib_list)
