def incomodam(n):
    if n <= 0:
        return ""
    frase = incomodam(n - 1) + "incomodam "
    return frase

def elefantes(n):
    if n < 2:
        return ""
    musica = ""
    musica += elefantes(n - 1)
    if n == 2:
        musica += "Um elefante incomoda muita gente\n"
        musica += str(n) + " elefantes " + incomodam(n) + "muito mais\n"
    else:
        musica += str(n - 1) + " elefantes incomodam muita gente\n"
        musica += str(n) + " elefantes " + incomodam(n) + "muito mais\n"
    return musica
