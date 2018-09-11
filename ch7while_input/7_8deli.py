#7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
#ous sandwiches. Then make an empty list called finished_sandwiches . Loop
#through the list of sandwich orders and print a message for each order, such
#as I made your tuna sandwich. As each sandwich is made, move it to the list
#of finished sandwiches. After all the sandwiches have been made, print a
#message listing each sandwich that was made.

sandwich_orders = ['reuben','pastrami', 'monte christo', 'grilled cheese',
                   'pastrami', 'pastrami', 'turkey']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich.title() + ".")
    finished_sandwiches.append(current_sandwich)

print("here's a list of all the sandwiches I made:")

for i in finished_sandwiches:
    print(i.title())
