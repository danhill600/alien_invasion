bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1])
#this syntax is quite useful, because you'll often want to return the last item of a list without knowing how long the list is.

message="My first proper bicycle was a " + bicycles[0].title() + "."
print(message)


