from domina import domina

def independentes(l):
    if not domina(l[0], l[1]) and not domina(l[1], l[0]):
        return True
    else:
        return False

print(independentes([[1,2],[0,1]]))