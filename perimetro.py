from comprimento import comprimento

def perimetro(p, q, r):
    l1 = comprimento(p,q)
    l2 = comprimento(p,r)
    l3 = comprimento(q,r)
    return l1 + l2 + l3