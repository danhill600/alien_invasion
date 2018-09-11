favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

friends = ['phil','sarah']
for name in friends:
    print(" Hi " + name.title() +
          ", I see your favoirte language is " +
          favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

should_take=['jesse','lord kromdor','jen','barton','phil','mr. matches']

for i in should_take:
    if i in favorite_languages.keys():
        print("Thanks for responding, " + i.title() + ".")
    else:
        print("Please take the poll, " + i.title() + ".")

