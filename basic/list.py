classmates = ["Michael", "Bob", "Tracy"]
print(classmates)
print(len(classmates))
print(classmates[-1])
# print(classmates[6])
# IndexError: list index out of range

print(range(5))
# range(0, 5)
print(list(range(5)))
# [0, 1, 2, 3, 4]

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# 5050

L = ["Bart", "Lisa", "Adam"]
for x in L:
    print(x)
