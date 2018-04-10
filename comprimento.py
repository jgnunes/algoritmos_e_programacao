def comprimento(p, q):
    delta_x = p[0] - q[0]
    delta_y = p[1] - q[1]
    distancia_pontos = (delta_x**2 + delta_y**2)**(1.0/2.0)
    return distancia_pontos

if __name__ == '__main__':
    print(comprimento([1,2],[1,2]))
    print(comprimento([1, 2], [1, 4]))
    print(comprimento([1, 3], [2, 5]))