def number_generator(n):
    for i in range(1, n + 1):
        yield i


print("Generator Values:")

for number in number_generator(10):
    print(number)


numbers = [i for i in range(1, 11)]

squares = [num ** 2 for num in numbers]

print("\nSquares using List Comprehension:")
print(squares)


print("\nUsing enumerate():")

for index, value in enumerate(squares, start=1):
    print(f"Index {index}: {value}")