
class Dog():
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = False
        
    def bark(self):
        return f'{self.name} est aboyant'
    
    def  run_speed(self):
        return f'{self.name} court à la vitesse {self.weight/self.age*10}'

    def fight(self, other_dog):
        if self.weight*(self.weight/self.age*10) > other_dog.weight*(other_dog.weight/other_dog.age*10):
            return f'{self.name} a gagné le combat'
        else:
            return f'{other_dog.name} a gagné le combat'
    
  
import random  
class  PetDog(Dog):
    
   def train(self):
       print(self.bark())
       self.trained = True
       
       
   def play(self, *args):
       for item in args:
            print(item, end=",")
       print("jouent ensemble")
           
   def do_a_trick(self):
       phrase = random.choice(["fait un rouleau de baril", "se tient sur ses jambes arrière", "secoue la main", "joue le mort"])   
       print(self.name,phrase)
    
chien = PetDog("Marley", 2, 15)
chien.train()
chien.play("Marley", "Oslo")
chien.do_a_trick()