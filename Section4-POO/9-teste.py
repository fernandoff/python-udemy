from Class.GameClass import Game

game1 = Game(
    name = "The Legend of Zelda: Breath of the Wild", 
    yearLaunch = 2017, 
    multiplayer = False, 
    note = 10
)

print("Game 1:")
game1.technical_sheet()

game2 = Game(
    name = "Fortnite", 
    yearLaunch = 2017, 
    multiplayer = True, 
    note = 8
)

print("Game 2:")
game2.technical_sheet()

game3 = Game()
print("Game 3:")
game3.technical_sheet()