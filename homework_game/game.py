import tkinter
class Char:
    def __init__(self, name, skill, hp, Iq, speed):
        self.name = name
        self.skill = skill
        self.hp = hp
        self.Iq = Iq
        self.speed = speed

    def upgrade_hp(self):
        cost = self.hp * 50
        if self.hp > 4:
            change_lvl()
        elif self.skill >= cost:
            self.hp = self.hp + 1
            self.skill = self.skill - cost
            change_Xp()
            change_Hp()
        else:
            not_enough()
        return self.hp

    def upgrade_iq(self):
        cost = self.Iq * 50
        if self.Iq > 4:
            change_lvl1()
        elif self.skill >= cost:
            self.Iq = self.Iq + 1
            self.skill = self.skill - cost
            change_Xp()
            change_iq()
        else:
            not_enough()
        return self.Iq

    def upgrade_speed(self):
        cost = self.speed * 50
        if self.speed > 4:
            change_lvl2()
        elif self.skill >= cost:
            self.speed = self.speed + 1
            self.skill = self.skill - cost
            change_Xp()
            change_speed()
        else:
            not_enough()
        return self.speed
character = Char("Warrior", 1000, 1, 1, 1)
window = tkinter.Tk()
window.title("game")
window.geometry("500x500")
title = tkinter.Label(text = "Upgrade skills", font= "Arial 24")
title.place(x=150, y=10)
name = tkinter.Label(text =character.name, font= "Arial 18")
name.place(x=15, y=50)
text = tkinter.Label(text = "XP= ", font= "Arial 16")
text.place(x=15, y=85)
Xp= tkinter.Label(text= str(character.skill), font= "Arial 16")
Xp.place(x=65, y=85)
def change_Xp():
    old_value = int(Xp["text"])
    Xp["text"] = str(character.skill)
button = tkinter.Button(fg= "green", text= "+", font= "Arial 28", command= character.upgrade_hp)
button.place(x=10, y=120)
text2 = tkinter.Label(text ="health ", font= "Arial 16")
text2.place(x=150, y=150)
hp = tkinter.Label(text =str(character.hp), font= "Arial 16")
hp.place(x=210, y=150)
def change_Hp():
    old_value = int(hp["text"])
    hp["text"] = str(character.hp)
text3 = tkinter.Label(text= "", font= "Arial 18")
text3.place(x=230, y=150)
def change_lvl():
    old = str(text3["text"])
    text3["text"] = str("Max level!")
button = tkinter.Button(fg= "green", text= "+", font= "Arial 28", command= character.upgrade_iq)
button.place(x=10, y=220)
text4 = tkinter.Label(text ="Iq ", font= "Arial 16")
text4.place(x=150, y=240)
iq = tkinter.Label(text =str(character.Iq), font= "Arial 16")
iq.place(x=210, y=240)
def change_iq():
    old_value = int(iq["text"])
    iq["text"] = str(character.Iq)
text5 = tkinter.Label(text= "", font= "Arial 18")
text5.place(x=230, y=240)
def change_lvl1():
    old = str(text5["text"])
    text5["text"] = str("Max level!")
button = tkinter.Button(fg= "green", text= "+", font= "Arial 28", command= character.upgrade_speed)
button.place(x=10, y=300)
text6 = tkinter.Label(text ="speed ", font= "Arial 16")
text6.place(x=150, y=320)
speed = tkinter.Label(text =str(character.speed), font= "Arial 16")
speed.place(x=210, y=320)
def change_speed():
    old_value = int(speed["text"])
    speed["text"] = str(character.speed)
text7 = tkinter.Label(text= "", font= "Arial 18")
text7.place(x=230, y=320)
def change_lvl2():
    old = str(text7["text"])
    text7["text"] = str("Max level!")
noXp = tkinter.Label(fg="red", text= "", font= "Arial 22")
noXp.place(x=185, y=80)
def not_enough():
    old = str(noXp["text"])
    noXp["text"] = str("not enough Xp!")
window.mainloop()

