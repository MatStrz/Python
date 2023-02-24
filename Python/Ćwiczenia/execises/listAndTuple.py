list = input("input a list of numbers")

print((list.split(",")))
print(tuple(list.split(",")))
list = list.split(",")

print(list)

reverse_list = list.copy()
reverse_list.reverse()
print(reverse_list)