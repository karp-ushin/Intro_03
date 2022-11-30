def decToBin(n):
    binary = ""
    while (n):
        reminder = n % 2
        binary += str(reminder)
        n //= 2
    binary = binary[:: -1]
    return binary
print(decToBin(45))
