def encontra_impares(lista, index = 0):
    impar = []
    if index >= len(lista):
        return impar

    i = 0
    for i in range(index, len(lista)):
        if lista[i] % 2 == 0:
            break
        else:
            impar.append(lista[i])
    impar.extend(encontra_impares(lista, i + 1))
    return impar
