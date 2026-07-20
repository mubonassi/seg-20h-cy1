#Break ; quit()

#Break encerra uma estrutura de repetição independente de seu estado
for i in range(100000000000):
    print(i)
    if i >= 5:
        break
print("Fim da repetição")

#quit() é uma função que ENCERRA o algoritmo
for i in range(100000):
    print(i)
    if i >= 5:
        quit()
print("Você não verá esse print")