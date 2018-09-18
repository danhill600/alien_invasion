#8-9. Magicians: Make a list of magician’s names. Pass the list to a function
#called show_magicians() , which prints the name of each magician in the list.

#8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
#Write a function called make_great() that modifies the list of magicians by add-
#ing the phrase the Great to each magician’s name. Call show_magicians() to
#see that the list has actually been modified.

#8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
#function make_great() with a copy of the list of magicians’ names. Because the
#original list will be unchanged, return the new list and store it in a separate list.
#Call show_magicians() with each list to show that you have one list of the origi-
#nal names and one list with the Great added to each magician’s name.

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    tempmagicians = []
    while magicians:
        current_magician = "The Great " + magicians.pop()
        tempmagicians.append(current_magician)
    while tempmagicians:
       magicians.append(tempmagicians.pop())
    return magicians

magicians = ['mortini','randy','mentaculus']

#make_great(magicians)
#show_magicians(magicians)

copymagicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(copymagicians)
