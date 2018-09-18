#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.

def make_shirt(size='Large', message='I <3 Python'):
    print("Your shirt size is: " + size + " and the message is '" +
          message + "'.")

make_shirt('Large','COLLGE')

make_shirt(size='xs',message='Honk if ur horny!')

make_shirt()
make_shirt('medium')
make_shirt('XXL',"Hey you get offa my cloud!")
