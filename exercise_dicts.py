def create_inventory(items):
    inventario = {}
    for item in items:
        inventario[item] = inventario.get(item, 0) + 1
    return inventario

def add_items(inventario, items):
    for item in items:
        inventario[item] = inventario.get(item, 0) + 1
    return inventario

def decrement_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] = max(0, inventario[item] - 1)
    return inventario

def remove_item(inventario, item):
    if item in inventario:
        del inventario[item]
    return inventario

def list_inventory(inventario):
    # Retorna lista de tuplas donde cantidad > 0
    return [(item, cant) for item, cant in inventario.items() if cant > 0]

def find_max_value(diccionario):
    if not diccionario:
        return ""
    # Retorna la clave del valor máximo
    return max(diccionario, key=diccionario.get)

def reverse_dict(diccionario):
    invertido = {}
    for k, v in diccionario.items():
        if v in invertido:
            invertido[v] += str(k)
        else:
            invertido[v] = str(k)
    return invertido

def word_frequency(palabras):
    freq = {}
    if not palabras: return freq
    for p in palabras:
        freq[p] = freq.get(p, 0) + 1
    return freq

def find_biggest_expense(gastos):
    if not gastos:
        return ""
    mejor_cat = ""
    max_promedio = -1
    for cat, montos in gastos.items():
        promedio = sum(montos) / len(montos) if montos else 0
        if promedio > max_promedio:
            max_promedio = promedio
            mejor_cat = cat
    return mejor_cat

def sum_expenses(gastos):
    return {cat: sum(montos) for cat, montos in gastos.items()}

def sum_expenses_by_type(gastos):
    resultado = {}
    for lista_tuplas in gastos.values():
        for tipo, monto in lista_tuplas:
            resultado[tipo] = resultado.get(tipo, 0) + monto
    return resultado