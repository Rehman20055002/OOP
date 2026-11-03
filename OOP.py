# class Soldier:
#     health = 100
#     uniform_color = "blue"

# soldier1 = Soldier()
# soldier2 = Soldier()

# Soldier.uniform_color = "green"

# soldier1.name = 'Cavad'
# soldier2.name = 'Aslan'

# soldier1.health = 110
# soldier2.health = 120

# print(soldier2.health)


# class Soldier:
#     health = 100
#     def __init__(self, uniform_color, power, name):
#         self.uniform_color = uniform_color
#         self.power = power
#         self.name = name


    # def fire(self, enemy_soldier):    def __mul__(self, enemy_soldier):
        # enemy_soldier.health = enemy_soldier.health - self.power
        # print(self.name, enemy_soldier.name, "ates acdi")

# soldier1 = Soldier(uniform_color = "green" , power = 30 , name = "Cavad")
# soldier2 = Soldier(uniform_color = "green" , power = 500, name = "Samir")

# soldier1.fire(soldier2)  soldier * soldier
# print(soldier2.health)


# class Player:
#     health = 100
#     def __init__(self,name):
#         self.name = name


# class Soldier(Player):
#     power = 20
#     def fire(self, player):
#         player.health = player.health - self.power


# class Doctor(Player):
#     treatment = 25
#     def treat(self, player):
#         player.health = player.health + self.treatment


# soldier = Soldier("Cavad")
# doctor = Doctor("Samir")

# soldier.fire(doctor)
# doctor.treat(soldier)

# print(soldier.health)



# class Silah:
#     metal = "silver"
#     def __init__(self, gulle_sayi):
#         self.gulle_sayi = gulle_sayi

    
# class Avtomat(Silah):
#     power = 20


# class Snayper(Silah):
#     power = 40


# class Soldier(Silah):
#     health = 100
#     def __init__(self,name,silah):
#         self.name = name
#         self.silah = silah

#     def fire(self, enemy):
#         enemy.health-=self.silah.power
#         self.gulle_sayi-=1


#     def __len__(self):
#         return self.silah.gulle_sayi


# Wiper = Snayper(7)
# Kalasnikov = Avtomat(30)

# samir = Soldier("Samir", Wiper)
# aslan = Soldier("Aslan", Kalasnikov)

# samir.fire(aslan)
# aslan.fire(samir)

# print(samir.health)