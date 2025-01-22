const agregarAlCarrito = document.getElementById("agregar-al-carrito");
const stockCantidad = document.getElementById("stock-cantidad");
const stockDisponible = document.getElementById("stock-disponible");

console.log(agregarAlCarrito, stockCantidad, stockDisponible);

// Tomar del localStorage
let shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
let virtualTotalStock =
    JSON.parse(localStorage.getItem("virtualTotalStock")) || {};

// Tomar id del producto
const productId =
    typeof selectedProductId !== "undefined" ? selectedProductId : null;

if (productId && stockCantidad) {
    const initialStock = parseInt(stockCantidad.textContent || "0", 10);
    if (!(productId in virtualTotalStock)) {
        virtualTotalStock[productId] = initialStock;
    }
}

function updateCartAmount() {
    const amountProducts = document.getElementById("amount-products-in-cart");
    if (!amountProducts) return;

    const shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
    let totalAmountInCart = 0;

    shoppingCart.forEach((product) => {
        totalAmountInCart += product.amount;
    });

    amountProducts.textContent = totalAmountInCart;
}

// WARN: Deberia sobreescribir lo que se manda del back porque al actualizarse la pagina vuelven a sumarse
function updateProductVirtualStock() {
    if (virtualTotalStock[productId] > 0) {
        virtualTotalStock[productId] -= 1;
        stockCantidad.textContent = virtualTotalStock[productId];
    }

    if (virtualTotalStock[productId] <= 0) {
        stockDisponible.textContent = "Agotado";
        stockDisponible.classList.remove("text-green-700");
        stockDisponible.classList.add("text-red-800");
        agregarAlCarrito.disabled = true;
        agregarAlCarrito.classList.remove(
            "bg-yellow-700",
            "hover:bg-yellow-800",
        );
        agregarAlCarrito.classList.add("bg-gray-400", "cursor-not-allowed");
    }
}
// WARN: no esta actualizando los agotados
function updateAllProductsVirtualStock() {
    const allProducts = document.querySelectorAll(".product");
    allProducts.forEach((product) => {
        const productId = product.getAttribute("href");
        const stockAgotado = product.querySelector("#stock-agotado");

        if (virtualTotalStock[productId] <= 0) {
            stockAgotado.classList.remove("hidden");
        }
    });
}

if (agregarAlCarrito) {
    agregarAlCarrito.addEventListener("click", async function () {
        try {
            const response = await fetch(`/api/stock/${productId}`);
            if (!response.ok)
                throw new Error("Error al obtener los datos del stock");

            const productData = await response.json();

            const fetchedId = productData.id;
            const fetchedTitle = productData.titulo;
            const fetchedStock = productData.stock;

            const productInCart = shoppingCart.find(
                (item) => item.id === fetchedId,
            );
            if (productInCart) {
                productInCart.amount += 1;
            } else {
                shoppingCart.push({
                    id: fetchedId,
                    amount: 1,
                    title: fetchedTitle,
                });
            }

            localStorage.setItem("shoppingCart", JSON.stringify(shoppingCart));
            localStorage.setItem(
                "virtualTotalStock",
                JSON.stringify(virtualTotalStock),
            );

            updateProductVirtualStock();

            updateAllProductsVirtualStock();
            updateCartAmount();
        } catch (error) {
            console.error("Error al cargar el producto al carrito:", error);
        }
    });
}

// Actualizar la cantidad del carrito al cargar la página
updateCartAmount();
updateAllProductsVirtualStock();
