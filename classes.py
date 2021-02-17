class Point():
   # magic method --init-- is going to be called every time we're going to create a  new point
   # self represents the object itself
    def __init__(self, input1, input2):
        self.x = input1 #the input value x is going to be stored in self object in the x variable
        self.y = input2

p = Point(2, 8) # calls the function Point and assigns values 2&8
   # x=2, y=8
print(p.x) # go into the point p, and access the value of variable x, and print it out
print(p.y)

class Flight():
    def __init__(self, capacity): # function that creates a new Flight
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name): # function that adds a new passenger if there are any seats left
        if not self.open_seats(): # same as open_seats ==0
            return False
        self.passengers.append(name)
        return True
    def open_seats(self): # function that returns the number of open seats
        return self.capacity - len(self.passengers)
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny", "McGaiver"]
for person in people:
    success = flight.add_passenger(person)
    if success:
         print (f"Added {person} to flight successfully")
    else:
     print(f"No available seats for {person}")
