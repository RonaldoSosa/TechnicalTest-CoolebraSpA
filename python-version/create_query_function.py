import sqlite3


def create_query():
    # Le da más prioridad al precio más bajo y si hay dos precios iguales, se queda con el más reciente
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("""
        WITH ActivePricesSorted 
        AS 
        (SELECT sku, ean, normal_price, create_date,
        ROW_NUMBER() OVER (PARTITION BY sku, ean ORDER BY normal_price ASC, create_date DESC) AS rank_price
        FROM Prices 
        WHERE active = 1) 
        SELECT ActivePricesSorted.sku, ActivePricesSorted.ean, Markets.name, Products.name, ActivePricesSorted.normal_price 
        FROM Markets, Products, ActivePricesSorted 
        WHERE Markets.sku = Products.sku AND Products.ean = ActivePricesSorted.ean AND ActivePricesSorted.sku = Products.sku AND ActivePricesSorted.rank_price = 1
        ORDER BY ActivePricesSorted.ean ASC;""")
    # Guardo los datos en una variable para la Pregunta 3
    data = cursor.fetchall()
    # Se cierra la conexión
    connection.close()
    return data
