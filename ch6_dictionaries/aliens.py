#alien_0= {'color':'green', 'points':5}
#alien_1={'color':'yellow','points':10}
#alien_2={'color':'red','points':15}
#
#aliens=[alien_0, alien_1, alien_2]
#
#for i in aliens:
#    print(i)

#A more likely scenerio:
#make an empty list for storing aliens.

aliens = []

#Make 30 green aliens

for i in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for i in aliens[0:3]:
    if i['color'] == 'green':
        i['color'] = 'yellow'
        i['speed'] = 'medium'
        i['points'] = 10


#Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

##Show how many aliens have been created.
#print("Total number of aliens:" + str(len(aliens)))

