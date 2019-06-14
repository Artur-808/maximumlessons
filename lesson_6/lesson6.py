import random
class Tank:
    def __init__(self, name,  armor, min_damage, max_damage, hp,):
        self.name = name
        self.armor = armor
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.hp = hp

    def run(self):
        print(self.name + " выдвигается")

    def loosehealth(self, damage):
        if self.hp <= 0:
            print("{} defeated".format(self.name))
        else:
            self.hp = self.hp - damage
            print("у {} осталось {} HP".format(self.name, self.hp))

    def fire(self, enemy):
        damage = random.randint(self.min_damage, self.max_damage)
        print("{} стреляет по {}".format(self.name, enemy.name))
        enemy.loosehealth(damage)

    def __str__(self):

        return "{} имеет броню в {}, урон {}-{}, и {} очков жизни".format(self.name, self.armor, self.min_damage, self.max_damage, self.hp)

if __name__ == "__main__":

    tank1 = Tank("Hellcat", 100, 15, 60, 300)
    tank2 = Tank("Panther", 80, 20, 70, 270)


    tank1.fire(tank2)

    for bullet in range(20):
        tank1.fire(tank2)