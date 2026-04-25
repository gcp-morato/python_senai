original = [10, 20, 30]

# Fatiamento completo = CÓPIA independente
copia = original[:]

copia[0] = 999
print(original)   # [10, 20, 30] → não mudou!
print(copia)      # [999, 20, 30] → só a cópia mudou