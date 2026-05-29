from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

tim = Player("Tim")

ugly_troll = Troll("Ugly")
print(ugly_troll)

another_troll = Troll("Ug")
print(another_troll)

brother = Troll("Urg")
print(brother)

enemy = Enemy()
print(enemy)

brother.grunt()
another_troll.grunt()
ugly_troll.grunt()

vamp = Vampyre("Vlad")
print(vamp)

while vamp.alive:
    vamp.take_damage(1)
    # print(vamp)

dracula = VampyreKing("Dracula")
print(dracula)

dracula.take_damage(12)
print(dracula)