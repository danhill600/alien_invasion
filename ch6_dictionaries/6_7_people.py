Ben = {
    'first_name':'Bennett',
    'last_name':'Foster',
    'age':35,
    'city':'Atlanta',
    }

Alice = {
    'first_name': 'Alice',
    'last_name': 'Rolls',
    'age':55,
    'city':'Atlanta',
}

Stephen = {
    'first_name': 'Stephen',
    'last_name': 'Spring',
    'age':50,
    'city':'Atlanta',
}
people = [Ben, Alice, Stephen]


#for i in people:
#    print("Name: " + i['first_name'].title() + " " + i['last_name'].title())
#    print("Age: " + str(i['age']))
#    print("City: " + i['city'])

for i in people:
    for j, k in i.items():
       print(str(j).title()  + ": " + str(k).title())
    print("---")
