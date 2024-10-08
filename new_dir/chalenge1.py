class Animal: 
   
   def __init__(self, name, age, nouriture ):
         self.name = name
         self.age = age 
         self.nouriture  = nouriture 
   def __eq__(self, other): 
        if isinstance(other, Student): 
            if other.name == self.name: 
                return True
        return False
         
   def move_the_cat(self):
        print("the animal is moving  ")      

class cat(Animal):
     def __init__(self, name, age, nouriture):
          super().__init__(name, age, nouriture)
        


anim1 = Animal("SCOOBYDO",23,"boons")

anim2 =  Animal("PENOKOYU",2,"MEAT")

