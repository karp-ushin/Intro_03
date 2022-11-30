from math import ceil
input_string = input("Enter a list elements separated by comma ")
input_list = input_string.split(",")
n = len(input_list)
int_list = []
for i in range(n):
    int_list.append(int(input_list[i]))
print([int_list[i]*int_list[n-1-i] for i in range(ceil(n/2))])
