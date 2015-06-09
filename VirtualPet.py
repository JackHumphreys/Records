#Virtual Pet

class VirtualPet:
    def __init__(self):
        self.name = None
        self.size = 0
        self.age = 0
        self.energy = 50
        self.favfoods = ["Lamb", "Chicken", "Beef", "Human"] 



    def eat(self, food):
        if food in self.favfoods:
            if food == self.favfoods[0]:
                self.energy = self.energy + 10
                print("Nice, but a bit on the fluffy side.")
            if food == self.favfoods[1]:
                self.energy = self.energy + 5
                print("Yum. Why did the chicken cross the road? It didn't I ate it.")
            if food == self.favfoods[2]:
                self.energy = self.energy + 20
                print("Delicious. Beef is my favourite.")
            if food == self.favfoods[3]:
                self.energy = self.energy + 15
                print("I wasn't even hungry just bored.")

    def sleep(self):
        if self.energy < 20:
            print("Pet is sleeping.")
            self.energy = self.energy + 30
        
            
PetOne = VirtualPet()

PetOne.name = input("Enter your pets name: ")
print()
print("Pet name has been changed to {0}".format(PetOne.name))
print()
print("Congratualtions!")
            
                
        





