def eleva_ao_quadrado(n):
    return n**2

def eleva_ao_cubo(n):
    return n**3

def eleva_a_6(n):
    return eleva_ao_quadrado(eleva_ao_cubo(2))

print(eleva_a_6(2))