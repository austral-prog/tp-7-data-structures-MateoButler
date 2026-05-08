def get_coordinate(registro):
    return registro[1]

def convert_coordinate(coordenada):
    return (coordenada[0], coordenada[1])

def create_record(registro_azara, registro_rui):
    # registro_rui[1] es la tupla ('4', 'B')
    # Convertimos la coord de Azara para comparar
    coord_azara_convertida = convert_coordinate(registro_azara[1])
    
    if coord_azara_convertida == registro_rui[1]:
        return (registro_azara[0], registro_azara[1], registro_rui[0], registro_rui[1], registro_rui[2])
    return "not a match"

def sum_tuple(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

def count_occurrences(tupla, elemento):
    count = 0
    for item in tupla:
        if item == elemento:
            count += 1
    return count

def find_index(tupla, elemento):
    for i in range(len(tupla)):
        if tupla[i] == elemento:
            return i
    return -1

def filter_positives(numeros):
    resultado = []
    for n in numeros:
        if n > 0:
            resultado.append(n)
    return tuple(resultado)