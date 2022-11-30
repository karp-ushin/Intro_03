def dec_to_bin(n):
    binary = ""
    while n:
        reminder = n % 2
        binary += str(reminder)
        n //= 2
    return binary[:: -1]


print(dec_to_bin(45))
