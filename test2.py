with open("../day_24_snake_game_adding_high_score/../.././Desktop/my_file.txt") as file:
    data = file.read()
    print(data)

with open("../day_24_snake_game_adding_high_score/../.././Desktop/my_file.txt", mode="a") as file:
    file.writelines("\nAm reusit!!!!!")

with open("../day_24_snake_game_adding_high_score/../.././Desktop/my_file.txt") as file:
    data1 = file.read()
    print(data1)
