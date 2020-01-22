def soma_lista(lista, index = 0):
    if index >= len(lista):
        return 0

    return lista[index] + soma_lista(lista, index + 1)
