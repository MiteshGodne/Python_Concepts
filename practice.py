# def recursive_transform(lst, index=0):
#     if index >= len(lst):
#         return
#     if lst[index] % 2 == 0:
#         lst[index] //= 2
#     else:
#         lst[index] = lst[index] * 3 + 1
#     recursive_transform(lst, index + 1)
# numbers = [5, 8, 3, 7, 10]
# recursive_transform(numbers)

# for i in range(len(numbers) - 1, -1, -1):
#     numbers[i] = numbers[i] - (numbers[i - 1] if i > 0 else 0)

# numbers = ("hello", "world", 5, 10, True)
# print(type(numbers))
# print(numbers)

print(type(eval(input())))

