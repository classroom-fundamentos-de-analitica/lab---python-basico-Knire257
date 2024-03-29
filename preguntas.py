"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum = 0
    data = open('data.csv', 'r').readlines()
    data_orgnized = [row.split() for row in data]
    column = [row[1] for row in data_orgnized]
    for num in column:
        sum += int(num) 
    return sum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    counter_dict = {}
    data = open('data.csv', 'r').readlines()
    data_orgnized = [row.split() for row in data]
    columns_of_interest = [row[0:2] for row in data_orgnized]
    for row in columns_of_interest:
        if row[0] in counter_dict:
            counter_dict[row[0]] += 1
        else:
            counter_dict[row[0]] = 1
    return sorted(counter_dict.items())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    counter_dict = {}
    data = open('data.csv', 'r').readlines()
    data_orgnized = [row.split() for row in data]
    columns_of_interest = [row[0:2] for row in data_orgnized]
    for row in columns_of_interest:
        if row[0] in counter_dict:
            counter_dict[row[0]] += int(row[1])
        else:
            counter_dict[row[0]] = int(row[1])
    return sorted(counter_dict.items())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    month_dict={}
    data = open('data.csv', 'r').readlines()
    data_orgnized = [row.split() for row in data]
    date_column = [row[2] for row in data_orgnized]
    month_column = [row.split('-')[1] for row in date_column]
    for month in month_column:
        if month in month_dict:
            month_dict[month] += 1
        else:
            month_dict[month] = 1 
    return sorted(month_dict.items())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dict_of_tuples = {} 
    data = open('data.csv', 'r').readlines()
    data_orgnized = [row.split() for row in data]
    columns_of_interest = [row[0:2] for row in data_orgnized]
    
    for row in columns_of_interest:
        if row[0] not in dict_of_tuples:
            dict_of_tuples[row[0]] = (row[0],int(row[1]),int(row[1]))
        else:
            if int(row[1]) > int(dict_of_tuples[row[0]][1]):
                dict_of_tuples[row[0]] = (row[0],int(row[1]),int(dict_of_tuples[row[0]][2]))
            elif int(row[1]) < int(dict_of_tuples[row[0]][2]):
                dict_of_tuples[row[0]] = (row[0],int(dict_of_tuples[row[0]][1]),int(row[1]))        
    return sorted(dict_of_tuples.values())


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    dict_of_tuples = {} 
    data = open('data.csv', 'r').readlines()
    dictionaries_per_row = [row.split()[4].split(',') for row in data]
    global_dictionary_list = []
    [global_dictionary_list.extend(dictionaries_per_row[i]) for i in range(len(dictionaries_per_row))]
    for item in global_dictionary_list:
        key,value = item.split(':')
        if key not in dict_of_tuples:
            dict_of_tuples[key] = (key,int(value),int(value))
        else:
            if int(value) < dict_of_tuples[key][1]:
                dict_of_tuples[key] = (key, int(value), dict_of_tuples[key][2])
            elif int(value) > dict_of_tuples[key][2]:
                dict_of_tuples[key] = (key, dict_of_tuples[key][1], int(value))
    return sorted(dict_of_tuples.values())


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    columns_of_interest = [row.split()[0:2] for row in data]
    dictionary_of_tuples = {}
    for item in columns_of_interest:
        value, key = item
        key = int(key)
        if key in dictionary_of_tuples:
            dictionary_of_tuples[key].append(value)
        else:
            dictionary_of_tuples[key] = [value]
    return sorted(dictionary_of_tuples.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    columns_of_interest = [row.split()[0:2] for row in data]
    dictionary_of_tuples = {}
    for item in columns_of_interest:
        value, key = item
        key = int(key)
        if key in dictionary_of_tuples:
            if value not in dictionary_of_tuples[key]:
                dictionary_of_tuples[key].append(value)
        else:
            dictionary_of_tuples[key] = [value]
    for item in dictionary_of_tuples:
        dictionary_of_tuples[item] = sorted(dictionary_of_tuples[item])
    return sorted(dictionary_of_tuples.items())


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dictionary = {} 
    data = open('data.csv', 'r').readlines()
    dictionaries_per_row = [row.split()[4].split(',') for row in data]
    global_dictionary_list = []
    [global_dictionary_list.extend(dictionaries_per_row[i]) for i in range(len(dictionaries_per_row))]
    global_dictionary_list = sorted(global_dictionary_list)
    for item in global_dictionary_list:
        key, value = item.split(':')
        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1
    return dictionary


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = open('data.csv', 'r').readlines()
    letter = [row[0] for row in data]
    set_of_letters = [row.split()[3].split(',') for row in data]
    column_with_dict = [row.split()[4].split(',') for row in data]
    list_of_tuples = []
    for i in range (len(letter)):
        list_of_tuples.append((letter[i],len(set_of_letters[i]),len(column_with_dict[i])))
    return list_of_tuples


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = open('data.csv', 'r').readlines()
    column_of_numbers = [row.split()[1] for row in data]
    column_of_letters = [row.split()[3].split(',') for row in data]
    dictionary = {}
    for i in range (len(column_of_letters)):
        for letter in column_of_letters[i]:
            key = letter
            value = int(column_of_numbers[i])
            if key not in dictionary:
                dictionary[key] = value
            else:
                dictionary[key] += value
    return {k: dictionary[k] for k in sorted(dictionary)}


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = open('data.csv', 'r').readlines()
    data = [row.split() for row in data]
    data_of_interest = [[row[0], sum([int(line.split(":")[1]) for line in row[4].split(",")])] for row in data]
    dictionary = {}
    for row in data_of_interest:
        key, value = row
        if key not in dictionary:
            dictionary[key] = value
        else:
            dictionary[key] += value
    return {k: dictionary[k] for k in sorted(dictionary)}

