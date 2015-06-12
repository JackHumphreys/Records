import random
class Crop:
    """A generic food crop"""

    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        #return a dictonary
        return {"light need" :self._light_need, "water need" :self._water_need}

    def report(self):
       return {"type" :self._type, "status" :self._status, "growth" :self._growth, "days growing" :self._days_growing}

    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seeds"

    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def auto_grow(crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)
    
def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter light value between 1-10: "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1-10: ")
        except ValueError:
            print("Value entered not valid - please enter a value between 1-10: ")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value between 1-10: "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1-10: ")
        except ValueError:
            print("Value entered not valid - please enter a value between 1-10: ")
    crop.grow(light,water)
            
def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report Status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected:
    
    
                

def main():
    #instaniate the class
    new_crop = Crop(1, 4, 3)
    print(new_crop.needs())
    print(new_crop.report())
    manual_grow(new_crop)
    print(new_crop.report())

if __name__ == "__main__":
    main()
