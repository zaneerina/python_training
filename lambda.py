
# nesting of structured data: dictionaries inside a list
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# people.sort() --> returns an error since python doesn't know how to sort the dictionary
""" instead of this:

def f(person):
    return person["name"] # returns the dictionaries sorted by name in alphabetical order
people.sort(key=f)

do this: """

people.sort(key= lambda person:person["name"]) # an actual function --> lambda person:person["name"]

print(people)