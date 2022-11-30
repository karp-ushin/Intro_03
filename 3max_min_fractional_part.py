my_list = [1.1, 1.2, 3.1, 5, 10.01]
min_frac_part = 1.
max_frac_part = 0.
for i in range(len(my_list)):
    frac_part = my_list[i] % 1
    if frac_part != 0.:
        if frac_part > max_frac_part:
            max_frac_part = frac_part
        elif frac_part < min_frac_part:
            min_frac_part = frac_part
if max_frac_part == 0.:
    print("No fractional parts")
else:
    print("Difference between maximum and minimum fractional parts is ", round(max_frac_part - min_frac_part, 2))
