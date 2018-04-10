from comprimento import comprimento
from perimetro import perimetro


def area(p, q, r):
    l1 = comprimento(p, q)
    l2 = comprimento(p, r)
    l3 = comprimento(q, r)
    s = perimetro(p, q, r)/2.0
    area = (s*(s-l1)*(s-l2)*(s-l3))**(1.0/2.0)
    return area

if __name__ == "__main__":
    print('área:', area([0, 1],[2, 4],[-7, 3]))