class Duck:
    def sound(self):
        return "Quack, quack!"
    
class AnotherBird:
    def sound(self):
        return "I'm similar to a duck!"

def make_it_sound(duck):
    print(duck.sound())

duck = Duck()
anotherBird = AnotherBird()
make_it_sound(duck)          # Outputs: Quack, quack!
make_it_sound(anotherBird)  # Outputs: I'm similar to a duck!