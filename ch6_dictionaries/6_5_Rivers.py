rivers = {
    'danube':'germany',
    'mississippi':'united states',
    'sangamon':'united states',
    'nile':'egypt',
    'amazon':'brazil',
}

for i,j in rivers.items():
    print("The " + i.title() + " river runs through " + j.title())

for i in rivers.keys():
    print(i.title())
print("\n")
for i in set(rivers.values()):
    print(i.title())
