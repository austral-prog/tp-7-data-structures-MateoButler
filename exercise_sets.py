def clean_ingredients(nombre_plato, ingredientes):
    return (nombre_plato, set(ingredientes))

def check_drinks(nombre_bebida, ingredientes):
    for ing in ingredientes:
        if ing in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"

def unique_chars(texto):
    return set(texto)

def sum_set(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

def common_elements(set_a, set_b):
    interseccion = set()
    for elemento in set_a:
        if elemento in set_b:
            interseccion.add(elemento)
    return interseccion