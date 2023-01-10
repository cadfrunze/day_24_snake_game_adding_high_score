
with open("data.txt", mode="r") as file:
    continut = file.read()


a = 5
with open("data.txt", mode="w") as file:
    file.write(str(a))

print(continut)





