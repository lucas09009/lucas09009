class Family():
    def __init__(self):
        self.membres = [
            {'name':'Michael',
             'age':35,
             'gender':'Male',
             'is_child':False,
             'power': 'fly',
             'incredible_name':'MikeFly'
            },
            {'name':'Sarah',
             'age':32,
             'gender':'Female',
             'is_child':False,
             'power': 'read minds',
             'incredible_name':'SuperWoman'
            }
            ]
        self.Nom_de_Famille = "ALOGNON"
        
        
    def born(self, **args):
        new_born = {**args}
        self.membres.append(new_born)
        print(self.membres)
        
    def is_18(self, name):
        liste_des_noms = []
        for item in self.membres:
            liste_des_noms.append(item["name"])
        if name not in liste_des_noms:
            return f"le nom saisi n'existe pas dans la liste des noms de la famille {self.Nom_de_Famille}"

        else:
            if item['age'] >= 18:
                return True
                
            else:
                return False
            
                
    def family_presentation(self):  
        for item in self.membres:
            print("\n",self.Nom_de_Famille, item["name"],"\n")
            
            
famille1 = Family()
famille1.born(name ="Abalo", age = 19, gender ='Male', is_child =True)
famille1.family_presentation()




class TheIncredibles(Family):
    def use_power(self):
        for item in self.membres:
            if self.age >= 18:
                print(item["name"],"a pour pouvoir",item["power"])
                
                
    def incredible_presentation(self):
        self.family_presentation()
        for item in self.membres:
            print(item["name"], "a pour pouvoir incroyable", item["power"])
            

    
incroyable = TheIncredibles()
incroyable.incredible_presentation()
incroyable.born(name="Baby Jack", power= "Inconnu")
incroyable.incredible_presentation()
print(incroyable.membres)
