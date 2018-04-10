from domina import domina

def dominados(l, p):
    dominados = []
    for ponto in l:
        if domina(p,ponto):
            dominados.append(ponto)

    return dominados

if __name__ == "__main__":
    print(dominados([[0,0],[2,-4],[4,4]], [3,3]))