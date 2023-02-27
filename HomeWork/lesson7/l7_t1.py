games = []
game = input("Введите игру: ")

while game != "0":
    if game not in games:
        games.append(game)
    else:
        print("Эта игра уже записана")
    game = input("Введите игру: ")

print(', '.join(sorted(games)))