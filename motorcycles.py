motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')

print(motorcycles)

motorcycles.insert(0,'ducaaaaaati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles.remove('yamaha')
print(motorcycles)
