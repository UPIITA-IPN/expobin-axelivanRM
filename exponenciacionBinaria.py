baseM = int(input("Introduce el valor de M: "))
expe = int(input("Introduce el valor de e: "))
modulon = int(input("Introduce el valor de n: "))

binario = format(expe, "b")
print(binario)

if binario[0] == "1":
    c = baseM
else:
    c = 1

k = len(binario) 
print(k)

a = 0
b = 0
ca = []
cb = []

for i in range(1, len(binario)):
    c = (c ** 2) % modulon
    ca.append(c)
    a += 1
    if binario[i] == "1":
        c = (c * baseM) % modulon
        cb.append(c)
        b += 1

print("Resultado:", c ,"\n")
print("Valores de c al cuadrado:", ca)
print("Valores de c multiplicados por M:", cb)
