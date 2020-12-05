#class MainGame:
    
class Pokemon:
    def __init__(name="James",level=1,hp=3,attack_stat=1,dodge=0):
        self.name=name
        self.level=level
        self.hp=hp
        self.attack_stat=attack_stat
        self.dodge=dodge
    def levelUp():
        print("Your pokemon has leveled up!")
        self.hp+=1
        self.attack_stat+=1
        choice=input('''Which stat do you want to increase?
1 for hp
2 for attack
3 for dodge
answer: ''')
        if choice==1:
            self.hp+=1
        elif choice==2:
            self.attack_stat+=1
        elif choice==3:
            self.dodge+=1
        else:
            print("wrong answer")
    def attack():
        ennemy.hp-=self.attack_stat
    #def mana():

poke=input("Name your pokemon!: ")
pokemon=Pokemon(poke)
