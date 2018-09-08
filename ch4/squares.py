squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# A little more concise:

squares = []

for value in range(1,11):
    squares.append(value**2)
print(squares)

#using list comprehension

squares = [value**2 for value in range(1,11)]
print(squares)
