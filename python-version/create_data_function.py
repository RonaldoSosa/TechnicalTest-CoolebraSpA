import sqlite3


def create_data():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # Se definen las tablas de la base de datos
    # Tabla Markets: sku, name
    cursor.execute(
        "CREATE TABLE Markets(sku INTEGER, name TEXT, PRIMARY KEY(sku))")
    # Tabla Products: sku, ean, name
    cursor.execute(
        "CREATE TABLE Products(sku INTEGER, ean INTEGER, name TEXT, UNIQUE(sku, ean), PRIMARY KEY(sku, ean), FOREIGN KEY(sku) REFERENCES Markets(sku))")
    # Tabla Prices: sku, ean, normal_price, discount_price, active, create_date
    cursor.execute("CREATE TABLE Prices(sku INTEGER, ean INTEGER, normal_price REAL, discount_price REAL, active BOOLEAN, create_date DATE, FOREIGN KEY(sku) REFERENCES Markets(sku), FOREIGN KEY(ean) REFERENCES Products(ean))")

    # Se insertan los datos de prueba
    # Datos para Markets
    marketsData = [(1, 'Ripley'), (2, 'Paris'), (3, 'Falabella')]
    # Datos para Products
    productsData = [
        (1, 1, 'Polera Nike'),
        (1, 2, 'Pantalon Levi'),
        (1, 3, 'Notebook Acer'),
        (1, 4, 'Polera Adidas'),
        (2, 1, 'Polera Nike'),
        (2, 2, 'Pantalon Levi'),
        (2, 3, 'Notebook Acer'),
        (2, 5, 'Zapatillas Puma'),
        (3, 1, 'Polera Nike'),
        (3, 2, 'Pantalon Levi'),
        (3, 3, 'Notebook Acer'),
        (3, 6, 'Reloj Casio')
    ]
    # Datos para Prices
    pricesData = [
        (1, 1, 15000, 13000, 0, '2023-12-10'),
        (1, 1, 18000, 16000, 1, '2023-12-11'),
        (1, 1, 20000, 18000, 1, '2023-12-12'),
        (1, 2, 10000, 9000, 0, '2023-12-01'),
        (1, 2, 12000, 10000, 1, '2023-12-02'),
        (1, 2, 15000, 13000, 1, '2023-12-03'),
        (1, 3, 500000, 450000, 0, '2023-12-01'),
        (1, 3, 550000, 500000, 1, '2023-12-02'),
        (1, 3, 600000, 550000, 1, '2023-12-03'),
        (1, 4, 15000, 13000, 0, '2023-12-01'),
        (1, 4, 18000, 16000, 1, '2023-12-02'),
        (1, 4, 20000, 18000, 1, '2023-12-03'),
        (2, 1, 19000, 18500, 0, '2023-12-03'),
        (2, 1, 20000, 19500, 1, '2023-12-04'),
        (2, 1, 21000, 20500, 1, '2023-12-05'),
        (2, 2, 11000, 10500, 0, '2023-12-08'),
        (2, 2, 12000, 11500, 1, '2023-12-09'),
        (2, 2, 13000, 12500, 1, '2023-12-13'),
        (2, 3, 510000, 505000, 0, '2023-12-01'),
        (2, 3, 520000, 515000, 1, '2023-12-02'),
        (2, 3, 530000, 525000, 1, '2023-12-03'),
        (2, 5, 10000, 9500, 0, '2023-12-01'),
        (2, 5, 11000, 10500, 1, '2023-12-02'),
        (2, 5, 12000, 11500, 1, '2023-12-03'),
        (3, 1, 18000, 17500, 0, '2023-12-03'),
        (3, 1, 19000, 18500, 1, '2023-12-04'),
        (3, 1, 20000, 19500, 1, '2023-12-05'),
        (3, 2, 10000, 9500, 0, '2023-12-08'),
        (3, 2, 11000, 10500, 1, '2023-12-09'),
        (3, 2, 12000, 11500, 1, '2023-12-13'),
        (3, 3, 500000, 495000, 0, '2023-12-01'),
        (3, 3, 510000, 505000, 1, '2023-12-02'),
        (3, 3, 520000, 515000, 1, '2023-12-03'),
        (3, 6, 100000, 95000, 0, '2023-12-01'),
        (3, 6, 110000, 105000, 1, '2023-12-02'),
        (3, 6, 120000, 115000, 1, '2023-12-03')
    ]

    # Markets: Ripley, Paris, Falabella
    cursor.executemany("INSERT INTO Markets VALUES(?, ?)", marketsData)
    # Products para los 3 markets
    cursor.executemany("INSERT INTO Products VALUES(?, ?, ?)", productsData)
    # Prices para los productos de los 3 markets
    cursor.executemany(
        "INSERT INTO Prices VALUES(?, ?, ?, ?, ?, ?)", pricesData)

    connection.commit()

    connection.close()
