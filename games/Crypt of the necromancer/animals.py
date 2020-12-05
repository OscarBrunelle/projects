class Animal:
    def __init__(self,species,language):
        self.spec=species
        self.lang=language

    def get(self):
        return (self.spec,self.lang)

    def speak(self):
        print("I'm a fuckin\'",self.spec,"and I motherfuckin\'",self.lang)


snoopy=Animal("dog","bark")
print(snoopy.lang)
#"super()." is to call a parent function

class Bird(Animal):
    '''extending'''
    def __init__(self,lenght_of_beak,species,language):
        self.lb=lenght_of_beak
        super().__init__(species,language)

    '''overriding'''
    def speak(self):
##        super().speak() -> extending
        print(3*self.lang)

twitter=Bird(15,"bird","chirp")
