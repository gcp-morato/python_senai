notas = [10000, 19990, 122220, 1111110, 11999120]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:5.2f}")