#make a list of three people you would invite to dinner
dreamlist=['sidrah','chris','matt']
print(dreamlist[0].title()+" you are cordially invited to dinner.")
print(dreamlist[1].title()+" you are cordially invited to dinner.")
print(dreamlist[2].title()+" you are cordially invited to dinner.")

print("\nUh oh. "+ dreamlist.pop().title()+" is getting his beard waxed, he can't come.")

dreamlist.append('Emily')

print("\n"+dreamlist[0].title()+" you are cordially invited to dinner.")
print(dreamlist[1].title()+" you are cordially invited to dinner.")
print(dreamlist[2].title()+" you are cordially invited to dinner.")

print("\n Oh nice, we just found a bigger table!")

dreamlist.insert(0,'Eric')
dreamlist.insert(2,'Sy')
dreamlist.append('Jeeves')

print(dreamlist[0].title()+" you are cordially invited to dinner.")
print(dreamlist[1].title()+" you are cordially invited to dinner.")
print(dreamlist[2].title()+" you are cordially invited to dinner.")
print(dreamlist[3].title()+" you are cordially invited to dinner.")
print(dreamlist[4].title()+" you are cordially invited to dinner.")
print(dreamlist[5].title()+" you are cordially invited to dinner.")
