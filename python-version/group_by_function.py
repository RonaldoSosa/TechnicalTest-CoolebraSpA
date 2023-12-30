def group_by_ean(data):
    ean_dict = dict()
    for element in data:
        if element[1] not in ean_dict:
            ean_dict[element[1]] = dict()
            ean_dict[element[1]]["Ean"] = element[3]
            ean_dict[element[1]]["data"] = list()
            ean_dict[element[1]]["data"].append(element)
            ean_dict[element[1]]["nMarkets"] = 1
            ean_dict[element[1]]["maxPrice"] = element[4]
            ean_dict[element[1]]["minPrice"] = element[4]
            ean_dict[element[1]
                     ]["priceRange"] = f"({ean_dict[element[1]]['maxPrice']} - {ean_dict[element[1]]['minPrice']})"
        else:
            ean_dict[element[1]]["data"].append(element)
            ean_dict[element[1]]["nMarkets"] += 1
            if element[4] > ean_dict[element[1]]["maxPrice"]:
                ean_dict[element[1]]["maxPrice"] = element[4]
            if element[4] < ean_dict[element[1]]["minPrice"]:
                ean_dict[element[1]]["minPrice"] = element[4]
            ean_dict[element[1]
                     ]["priceRange"] = f"({ean_dict[element[1]]['maxPrice']} - {ean_dict[element[1]]['minPrice']})"
    # Se crea una lista con los datos de los productos de acuerdo a lo solicitado en el enunciado
    ean_list = list()
    for key in ean_dict:
        ean_list.append(ean_dict[key])
    # Se retorna la lista
    return ean_list
