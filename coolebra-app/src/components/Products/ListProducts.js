import React, { useState, useEffect } from "react";
import "./style.css";
import productsData from "../../data/productsData";

function ListProducts() {
    const [dataProducts, setDataProducts] = useState(productsData);
    const [currentValue, setCurrentValue] = useState("");

    useEffect(() => {
        const intervalId = setInterval(() => {
            const filteredProducts = dataProducts.filter((product) =>
                product.Ean.toLowerCase().includes(currentValue.toLowerCase())
            );
            const indexToRemove = dataProducts.findIndex(
                (product) => !filteredProducts.includes(product)
            );
            if (indexToRemove !== -1) {
                const updatedProducts = dataProducts.filter(
                    (product) => product !== dataProducts[indexToRemove]
                );
                setDataProducts(updatedProducts);
            }
        }, 1000);

        if (currentValue === "") {
            setDataProducts(productsData);
        }

        return () => clearInterval(intervalId);
    }, [dataProducts, currentValue]);

    return (
        <>
            <h1> Buscador de Productos</h1>
            <div className="inputContainer">
                <input
                    type="text"
                    value={currentValue}
                    onChange={(e) => setCurrentValue(e.target.value)}
                />
            </div>

            <h2> Lista de Productos</h2>
            <div className="productListContainer">
                {dataProducts.map((product) => (
                    <div className="componentListProduct" key={product.Ean}>
                        <p className="subtitle">Nombre:</p>
                        <p className="content">{product.Ean}</p>
                        <p className="subtitle">Rango de Precio:</p>
                        <p className="content">{product.priceRange}</p>
                        <p className="subtitle">Mercados:</p>
                        <p className="content">Disponible en {product.nMarkets} mercados</p>
                    </div>
                ))}
            </div>
        </>
    );
}

export default ListProducts;
